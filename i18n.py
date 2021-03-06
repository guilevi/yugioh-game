import gettext
import re
import duel as dm
import game

def set_language(con, language):
	if language == 'en':
		con.cdb = dm.db
		con._ = gettext.NullTranslations().gettext
		con.language = 'en'
	elif language == 'de':
		con.cdb = game.german_db
		con._ = gettext.translation('game', 'locale', languages=['de'], fallback=True).gettext
		con.language = 'de'
	elif language == 'ja':
		con.cdb = game.japanese_db
		con._ = gettext.translation('game', 'locale', languages=['ja'], fallback=True).gettext
		con.language = 'ja'
	elif language == 'es':
		con.cdb = game.spanish_db
		con._ = gettext.translation('game', 'locale', languages=['es'], fallback=True).gettext
		con.language = 'es'

def parse_strings(filename):
	res = {}
	with open(filename, 'r', encoding='utf-8') as fp:
		for line in fp:
			line = line.rstrip('\n')
			if not line.startswith('!'):
				continue
			type, id, s = line[1:].split(' ', 2)
			if id.startswith('0x'):
				id = int(id, 16)
			else:
				id = int(id)
			if type not in res:
				res[type] = {}
			res[type][id] = s.replace('\xa0', ' ')
	return res
