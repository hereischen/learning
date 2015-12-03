import MySQLdb as dbapi
import csv
import os


dbServer = 'server'
dbPass = 'your passwd'
# dbSchema = 'payment2'
dbUser = 'your username'

dbQuery = 'SELECT * FROM payment2.trades_transaction WHERE transaction_time >= "2015-12-01" AND  transaction_time <= "2015-12-05 23:59";'

db = dbapi.connect(host=dbServer, user=dbUser, passwd=dbPass)
cur = db.cursor()
cur.execute(dbQuery)
result = cur.fetchall()

file_dir = os.path.dirname(__file__)
file_name = 'cooldata.csv'
cool_location = os.path.join(file_dir, file_name)

print 'saving data >>> ' + cool_location
c = csv.writer(open(cool_location, "wb"))
for row in result:
    c.writerow(row)

print 'feeling cool'
