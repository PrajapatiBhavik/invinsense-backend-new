#from pymysql import NULL
#from pyparsing import empty
import config
#import pymysql
#from db import mysql
from flask import request, session
from flask_cors import cross_origin
import models.database


# function for getting logged in username from the cookie
@cross_origin(supports_credentials=True)
def giveNameOfUser():
	username = ''
	if request.cookies.get('user'):
		username = request.cookies.get('user')
		if '%20' in username:
			username = username.replace('%20',' ')
		print(username)
	else:
		username = "Anonymous"
	print(type(username))
	print(username)
	return username


# getting current request header information
def track_visitor():
	if not config.is_tracking_allowed():
		return
	else:
		ip_address = request.remote_addr
		requested_url = request.url
		referer_page = request.referrer
		page_name = request.path
		query_string = request.query_string
		user_agent = request.user_agent.string
		method = request.method
		toolName = page_name[1:]
		tools = ["Wazuh","Shuffle","TheHive","Infopercept","MISP","DejaVu","Ansible","Deceptive Bytes","DefectDOJO","Caldera","Infection Monkey","RedELK","Scout","SimpleRisk","Rukovoditel"]

		if toolName not in tools:
			toolName = "Annonymous"
			
		username = giveNameOfUser().get_data().decode()
		print(username)
		if config.track_session():
			log_id = session['log_id'] if 'log_id' in session else 0
			no_of_visits = session['no_of_visits']
			current_page = request.url
			previous_page = session['current_page'] if 'current_page' in session else ''
			
			if previous_page != current_page:
				log_visitor(ip_address, requested_url, referer_page, page_name, query_string, user_agent, no_of_visits,method,username,toolName)
		else:			
			conn = None
			cursor = None
			session.modified = True
			
			try:				
				conn = models.database.createConnection()
				cursor = conn.cursor()
				
				log_id = log_visitor(ip_address, requested_url, referer_page, page_name, query_string, user_agent,method,username,toolName)
				
				#print('log_id', log_id)
				
				if log_id > 0:				
					sql = 'select max(no_of_visits) as next from visits_log limit 1'
					
					conn = models.database.createConnection()
					print(conn)
					cursor = conn.cursor(conn.cursors.DictCursor)
					
					cursor.execute(sql)
					row = cursor.fetchone()
					
					count = 0
					if row['next']:
						count += 1
					else:
						count = 1
					
					sql = 'UPDATE visits_log set no_of_visits = %s WHERE log_id = %s'
					data = (count, log_id,)
					
					cursor.execute(sql, data)
					
					conn.commit()
					
					session['track_session'] = True
					session['no_of_visits'] = count
					session['current_page'] = requested_url
				else:
					session['track_session'] = False
			except Exception as e:
				print(e)
				session['track_session'] = False
			# finally:
			# 	cursor.close()
			# 	conn.close()
				


# function for catch up request header information and insert into the mariadb database
def log_visitor(ip_address, requested_url, referer_page, page_name, query_string, user_agent, method ,username, toolName ,no_of_visits=None):
	sql = None
	data = None
	conn = None
	cursor = None
	log_id = 0
	
	if no_of_visits == None:
		sql = "INSERT INTO visits_log(no_of_visits, ip_address, requested_url, referer_page, page_name, query_string, method, user_agent, username, tool_name) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
		data = (no_of_visits, ip_address, requested_url, referer_page, page_name, query_string, method ,user_agent,username,toolName)
	else:
		sql = "INSERT INTO visits_log(ip_address, requested_url, referer_page, page_name, query_string, method ,user_agent, username, tool_name) VALUES(%s, %s, %s, %s, %s, %s ,%s, %s, %s)"
		data = (ip_address, requested_url, referer_page, page_name, query_string, method ,user_agent,username,toolName)
	
	try:				
		conn = models.database.createConnection()
		print(conn)
		cursor = conn.cursor()
		if page_name == '/tracking_report':
			pass
		else:
			cursor.execute(sql, data)
					
		conn.commit()
		log_id = cursor.lastrowid
		
		return log_id
	except Exception as e:
		print(e)
	# finally:
	# 	cursor.close()
	# 	conn.close()

