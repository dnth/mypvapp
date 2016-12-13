
import pymysql

hostname = 'localhost'
username = 'root'
password = 'root'
database = 'myprovi'

print "Initiating Connection"
myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
print "Connected!"

cursor = myConnection.cursor()     # get the cursor


try:
	
	with myConnection.cursor() as cursor:
		sql = "SELECT * FROM `user_pass` "
		cursor.execute(sql)
		result = cursor.fetchone()
		print result

except:
   	print ("Error: unable to fecth data")


myConnection.close()
print "Connection closed"
