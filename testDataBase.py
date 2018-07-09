import sqlite3 

sqlite3.version
sqlite3.sqlite_version
conn = sqlite3.connect("banco.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS tbEquipe (Nome text, Funcao text)""")

# insere alguns dados
cursor.execute("INSERT INTO tbEquipe VALUES ('Adriano', 'Eng')")
# salva dados no banco
conn.commit()


# insere múltiplos registros de uma só vez usando o método "?", que é mais seguro
tbEquipe =[('Marco', 'Analist'),
           ('Camila', 'Manager')]
cursor.executemany("INSERT INTO tbEquipe VALUES (?,?)", tbEquipe)
conn.commit()

# consulta
print ("----------------------------------")
sql = "SELECT * FROM tbEquipe WHERE Nome=?"
cursor.execute(sql, [("Adriano")])
print (cursor.fetchall())  # ou use fetchone()


print ("\nAqui a lista de todos os registros na tabela:\n")
for row in cursor.execute("SELECT rowid, * FROM tbEquipe ORDER BY Nome"):
   print (row)


print ("\nResultados de uma consulta com LIKE:\n")
sql = """
SELECT * FROM tbEquipe
WHERE Nome LIKE 'M%'"""
cursor.execute(sql)
print (cursor.fetchall())



