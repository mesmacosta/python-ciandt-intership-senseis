import datetime
import uuid
import yaml
import json
import re

from random import randint
from repository import save_game, new_game, get_game

MAX_TRIRES = 6

__all__ = ['start_game', 'gess_word', 'reset_game']

def gess_word(_id: str, gess: str):
	data = get_game(_id)

	if data.get('result', None):
		return data

	word = data['word']
	find = data['find']

	findings = [m.start() for m in re.finditer(gess.lower(), word.lower())]
	for idx in findings:
		find = find[:idx] + gess + find[idx+1:]

	data['find'] = find
	if find.find('_') < 0:
		data['result'] = 'win'

	print(json.dumps(data, indent = 3))
	if data['tries'] + 1 > MAX_TRIRES:
		data['result'] = 'lose'

	save_game(_id, data)

	return data
	
def new_id():
	return uuid.uuid1()

def reset_game(_id):
	return 'success'

def start_game(_id):
	word = HANGMAN_DATA[2]
	find = word

	for a in word:
		if a != ' ':
			find = find.replace(a, '_')

	data = new_game({
		_id: {
			'word': word,
			'find': find,
			'tries': 0,
			'result': ''
		}
	})

	return data[_id]

HANGMAN_DATA = [
	"Alura",
	"Business Complexity Points",
	"Driven by Impact",
	"Drupalize me",
	"Gestão Financeira",
	"Financial Management",
	"Gemba Walk Data driven mindset",
	"Hoshin Kanri",
	"Lean Digital Transformation",
	"Introduction to Lean Leadership",
	"Lifelong Learning",
	"Mindset Data Driven",
	"O Reilly",
	"Pluralsight",
	"Jira Poka Yoke",
	"Powerful Stories Bradesco Seguros",
	"Powerful Stories Cielo",
	"Powerful Stories iHeartMedia",
	"Powerful Stories Konica Minolta",
	"Powerful Stories Porto Seguro",
	"Powerful Stories Raizen",
	"Powerful Stories VIVO",
	"Introduction to Product Management",
	"Our Unfinished Journey",
	"Journey and Ambiguity",
	"Lean Startup Week"
]


if __name__ == '__main__':
	import pprint

	_id = str(uuid.uuid1())
	pprint.pprint(start_game(_id))
	gess_word(_id, 'D')
	gess_word(_id, 'i')
	gess_word(_id, 'r')
	gess_word(_id, 'b')
	gess_word(_id, 'm')
	gess_word(_id, 'p')
	gess_word(_id, 'a')
	gess_word(_id, 'c')
	gess_word(_id, 'e')
	gess_word(_id, 'n')
	gess_word(_id, 'p')
	gess_word(_id, 'y')
	gess_word(_id, 'v')
	gess_word(_id, 't')
	pprint.pprint(gess_word(_id, 'I'))