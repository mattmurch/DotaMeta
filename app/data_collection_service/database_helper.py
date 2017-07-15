import sqlite3

class Helper(object):
	
	def __init__(self):
		self.conn = sqlite3.connect('../../data/example.db')
		self.c = self.conn.cursor()
	
	def create_match_table(self):
		self.c.execute(
		'''
		CREATE TABLE matches (
			timestamp integer,
			match_id integer,
			match_seq_num integer,
			start_time integer,
			lobby_type integer,
			account_id integer
		)
		''')
		
	def create_player_table(self):
		self.c.execute(
		'''
		CREATE TABLE players (
			timestamp integer,
			account_id integer,
			player_slot integer,
			hero_id integer
		)
		''')

	def map_json_to_matches_table_schema(response):
		for field in response.iteritems():
			if "matches" in field:
				columns = ['timestamp', 'match_id', 'match_seq_num', 
				'start_time', 'lobby_type', 'account_id']
				print(field)
				for data in field:
					keys = tuple(data[c] for c in columns)
					print(keys)
				
	def commit_match_history_data(self, match_keys, player_keys):
		"""Puts the keys which we get from the get_match_history call
		into the database under the correct table."""
		self.c.execute('INSERT INTO matches VALUES (?,?,?,?,?)', match_keys)
		self.c.execute('INSERT INTO players VALUES (?,?,?)', player_keys)
		self.conn.commit()

	def close(self):
		self.conn.close()
