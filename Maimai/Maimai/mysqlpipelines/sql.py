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
	def insert_baseitem(self, id, name, sex, birthday, img, company, position, work_city, birth_city, xingzuo, tag, url):
		sql = 'INSERT INTO baseitem (ID, NAME, SEX, BIRTHDAY, IMG, COMPANY, POSITION, WORK_CITY, BIRTH_CITY, XINGZUO, TAG, URL) VALUES (%(id)s, %(name)s, %(sex)s, %(birthday)s, %(img)s, %(company)s, %(position)s, %(work_city)s, %(birth_city)s, %(xingzuo)s, %(tag)s, %(url)s)'
		value = {
			'id' : id,
			'name' : name,
			'sex' : sex,
			'birthday' : birthday,
			'img' : img,
			'company' : company,
			'position' : position,
			'work_city' : work_city,
			'birth_city' : birth_city,
			'xingzuo' : xingzuo,
			'tag' : tag,
			'url' : url,
			}
		cur.execute(sql, value)
		cnx.commit()

	@classmethod
	def insert_workitem(self, id, company, position, description, start_date, end_date):
		sql = 'INSERT INTO workitem (ID, COMPANY, POSITION, DESCRIPTION, START_DATE, END_DATE) VALUES (%(id)s, %(company)s, %(position)s, %(description)s, %(start_date)s, %(end_date)s)'
		value = {
			'id' : id,
			'company' : company,
			'position' : position,
			'description' : description,
			'start_date' : start_date,
			'end_date' : end_date,
			}
		cur.execute(sql, value)
		cnx.commit()

	@classmethod
	def insert_eduitem(self, id, school, degree, department, start_date, end_date):
		sql = 'INSERT INTO eduitem (ID, SCHOOL, DEGREE, DEPARTMENT, START_DATE, END_DATE) VALUES (%(id)s, %(school)s, %(degree)s, %(department)s, %(start_date)s, %(end_date)s)'
		value = {
			'id' : id,
			'school' : school,
			'degree' : degree,
			'department' : department,
			'start_date' : start_date,
			'end_date' : end_date,
			}
		cur.execute(sql, value)
		cnx.commit()

	@classmethod
	def insert_commentitem(self, id, friend_id, friend_name, friend_company, friend_position, level, comment):
		sql = 'INSERT INTO commentitem (ID, FRIEND_ID, FRIEND_NAME, FRIEND_COMPANY, FIREND_POSITION, LEVEL, COMMENT) VALUES (%(id)s, %(friend_id)s, %(friend_name)s, %(friend_company)s, %(firend_position)s, %(level)s, %(comment)s)'
		value = {
			'id' : id,
			'friend_id' : friend_id,
			'friend_name' : friend_name,
			'friend_company' : friend_company,
			'friend_position' : friend_position,
			'level' : level,
			'comment' : comment,
			}
		cur.execute(sql, value)
		cnx.commit()
