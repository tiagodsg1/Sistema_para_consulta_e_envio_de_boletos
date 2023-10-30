import psycopg2 

def servidor():
    try: 
        servidor = psycopg2.connect(
            user = 'postgres',
            password = '1234',
            host = 'localhost',
            port = '5432',
            database = 'UpHouse'
        )
        print('Conectado ao banco de dados')
        cursor = servidor.cursor()
        insert_query = ("""INSERT INTO Clientes (Nome, CPF, Telefone, Email, Endereco, Data_Vencimento) VALUES (%s, %s, %s, %s, %s, %s);""")
        dados = [
            ('João', '123456789', '123456789', 'joao@gmail.com', 'Rua 1', '2021-10-24'),
            ('Maria', '987654321', '987654321', 'Maria@gmail.com', 'Rua 2', '2021-10-24'),
            ('José', '123456789', '123456789', 'jose@gmail.com', 'Rua 3', '2021-10-24')]
        
        for dado in dados:
            cursor.execute(insert_query, dado)
        servidor.commit()

    except(Exception, psycopg2.Error) as error:
        print('Erro ao inserir dados', error)

    finally:
        if servidor:
            cursor.close()
            servidor.close()
            print('Conexão encerrada')
    
servidor()
