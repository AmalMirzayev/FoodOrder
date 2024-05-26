import mysql.connector
connection = mysql.connector.connect(host = "localhost", user = "root", password = "Amal1234", database = "Course")
cursor = connection.cursor(dictionary = True)



