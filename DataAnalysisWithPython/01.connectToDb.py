from dmodule import connect

# Create connection object 
connection = connect ('databasename', 'username', 'pwd')

# Create a cursor object 
cursor = connection.cursor()

# Run queries
cursor.execute('select * from mytable')
results = cursor.fetchall()

# Free resources
cursor.close()
connection.close()