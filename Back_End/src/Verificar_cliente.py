import psycopg2

def verificar_cliente():

    servidor = psycopg2.connect(
        user= 'postgres',
        password= '1234',
        host= 'localhost',
        port= '5432',
        database= 'UpHouse'
    )
    cursor = servidor.cursor()
    id = 1
    cursor.execute("SELECT * FROM Clientes")
