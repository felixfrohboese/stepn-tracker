import psycopg2

connection = psycopg2.connect('dbname=cmcdata2')

cursor = connection.cursor()


cursor.execute('SELECT * FROM table2;')
#cursor.rollback()


result = cursor.fetchall()
result = cursor.fetchone()
result = cursor.fetchmany(2)

print('fetchmany(2)', result)

data = {
  'id': result[],
  'completed': result[]
}



connection.commit()

connection.close()
cursor.close()
