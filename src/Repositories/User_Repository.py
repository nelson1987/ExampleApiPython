import sqlite3
class UserRepository:
    def ListarUsuarios():
        """Listar Usuarios"""
        conn = sqlite3.connect('exemplo.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM 'user'")
        resultados = cursor.fetchall()
        cursor.close()
        conn.close()
        return resultados
    
    def CriarUsuario(model):
        """Criar Usuarios"""
        # Validar o comando
        if model.title == '':
            raise Exception('Nome do usuário é obrigatório.')
        
        if model.description == '':
            raise Exception('E-mail do usuário é obrigatório.')
        
        if model.done == '':
            raise Exception('Senha do usuário é obrigatória.')

        conn = sqlite3.connect('nome_do_arquivo.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO clientes (nome, idade) VALUES (?, ?)", (model.title, 30))

        conn.commit()
        conn.close()



