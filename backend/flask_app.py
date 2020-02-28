"""Main a pp."""
# pylint: disable-msg=C0103,C0413,C0412,R0401
from os import getenv
from os.path import join, dirname

import connexion
import yaml
from dotenv import load_dotenv
from flask_migrate import Migrate
from jinja2 import Environment, PackageLoader

from backend.adapters.endpoints.config_flask import custom_flask
from backend.adapters.endpoints.public_api_flask.jinja.custom_filters import (
    get_all_apis_router,
    get_entity_fields,
)


SWAGGER_PATH = "swagger/"
API_PATH = ".".join(SWAGGER_PACK)

app = connexion.App(__name__, specification_dir=SWAGGER_PATH)
application = app.app
application.url_map.strict_slashes = False

# setting before request
custom_flask(application)

_env = Environment(loader=PackageLoader(".", "swagger"))
swagger_string = _env.get_template("main.yaml").render(
    lstrip=False,
    api=get_all_apis_router("api", SWAGGER_PATH),
    schemas=get_all_apis_router("schemas", SWAGGER_PATH),
    **get_entity_fields(),
)

specification = yaml.safe_load(swagger_string)

API_PATH += ".api"

app.add_api(
    specification,
    resolver=connexion.RestyResolver(API_PATH),
    options={"swagger_ui": application.config.get("SWAGGER_UI")},
)



