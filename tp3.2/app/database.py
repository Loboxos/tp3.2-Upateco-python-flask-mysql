import mysql.connector
connection = mysql.connector.connect(
 host='127.0.0.1',
 user='my_user',
 port = "3306",
 password='my_pass',
 database='my_database'
 )