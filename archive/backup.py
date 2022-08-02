@app.route('/todos/create', method=['POST'])
def create_todo():
  description = request.form.get('description', '')
  todo = Todo(description=description)
  db.session.add(todo)
  db.session.commit()
  return redirect(url_for('index'))

###


import psycopg2

connection = psycopg2.connect('dbname=cmcdata')

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table2;')

cursor.execute('''
  CREATE TABLE table2 (
    id INTEGER PRIMARY KEY,
    completed BOOLEAN NOT NULL DEFAULT False
  );
''')

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (1, True))

SQL = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'

data = {
  'id': 2,
  'completed': False
}
cursor.execute(SQL, data)

connection.commit()

connection.close()
cursor.close()


######

def execute_print_query(sql_statement):
    """
    Returns the query formatted as a Pandas' dataframe.

    Parameters
    -----------
    sql_statement : string
        The string containing the desired SQL statement to run.

    Returns
    --------
    pandas.DataFrame
    """

    query = engine.execute(sql_statement)
    return pd.DataFrame(query.fetchall(), columns=query.keys())
