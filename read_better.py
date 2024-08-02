import yaml
import mysql.connector
"""
The safe_load() function of PyYAML module loads
a YAML file with object serialization
"""
db= yaml.safe_load(open('db.yaml'))
"""
We use the information inside the YAML file to configure something
similar to the connection string, which is then loaded into our
connector to create our connection
"""
config = {
    'user':     db['user'],
    'password':  db['pwrd'],
    'host':      db['host'],
    'database':  db['db'],
    'auth_plugin': 'mysql_native_password'
}
cnx = mysql.connector.connect(**config)

cursor = cnx.cursor()
query = ("SELECT * FROM colleges")
cursor.execute(query)

# print all the rows
for row in cursor.fetchall():
    print(row)

cursor.close()
cnx.close()    