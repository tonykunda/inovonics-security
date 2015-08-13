import pymysql
import database_creds

class DatabaseCommunication(object):
	def __init__(self):
		self.connection = pymysql.connect(host=database_creds.host, db=database_creds.database, user=database_creds.username, passwd=database_creds.password, autocommit = True)

	def write(self, query):
		cur = self.connection.cursor()
		last_id = cur.execute(query)
		cur.close()
		return last_id

	def all(self, query):
		result = []
		cur = self.connection.cursor()
		cur.execute(query)
		for row in cur:
			result.append(row)
		cur.close()
		return result

	def single_column(self, query):
		result = []
		cur = self.connection.cursor()
		cur.execute(query)
		for row in cur:
			result.append(row[0])
		cur.close()
		return result

	def single_row(self, query):
		cur = self.connection.cursor()
		cur.execute(query)
		result = cur.fetchone()
		cur.close()
		return result

	def single_cell(self, query):
		cur = self.connection.cursor()
		cur.execute(query)
		result = cur.fetchone()[0]
		cur.close()
		return result