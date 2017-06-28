# coding=utf-8

import MySQLdb

MYSQL_HOSTS = 'localhost'
MYSQL_USER = 'maimai'
MYSQL_PASSWORD = 'maimai'
MYSQL_PORT = 3306
MYSQL_DB = 'maimai'

cnx = MySQLdb.connect(user=MYSQL_USER, passwd=MYSQL_PASSWORD, host=MYSQL_HOSTS, db=MYSQL_DB, port=MYSQL_PORT, charset='utf8')
cur = cnx.cursor()

class Sql:
	
	@classmethod
	def insert_baseitem(self, id, name, sex, birthday, img, description, work_city, birth_city, xingzuo):
		sql = 'INSERT INTO baseitem (ID, NAME, SEX, BIRTHDAY, IMG, DESCRIPTION, WORK_CITY, BIRTH_CITY, XINGZUO) VALUES (%(id)s, %(name)s, %(sex)s, %(birthday)s, %(img)s, %(description)s, %(work_city)s, %(birth_city)s, %(xingzuo)s)'
		value = {
			'id' : id,
			'name' : name,
			'sex' : sex,
			'birthday' : birthday,
			'img' : img,
			'description' : description,
			'work_city' : work_city,
			'birth_city' : birth_city,
			'xingzuo' : xingzuo
			}
		cur.execute(sql, value)
		cnx.commit()

