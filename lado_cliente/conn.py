import mysql.connector

try:
    banco = mysql.connector.connect(
        host='localhost',
        database='python',
        user='root',
        password=''
    )
except mysql.connector.Error as e:
    print("Erro de conexão com o servidor", e)
    


