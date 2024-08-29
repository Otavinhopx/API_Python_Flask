import sqlite3

connection = sqlite3.connect('banco.db')
cursor = connection.cursor()

cria_tabela= "CREATE TABLE IF NOT EXISTS fruta (fruta_id text PRIMARY KEY, \
    nomeFruta text, corFruta text, precoFruta real)"
    
cria_fruta = "INSERT INTO fruta VALUES ('laranja', 'laranja', 'laranja', 4.20)"
    
cursor.execute(cria_tabela)
cursor.execute(cria_fruta)

connection.commit()
connection.close()