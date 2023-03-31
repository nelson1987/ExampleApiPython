class UsuarioService:
    def Criar_Usuario(self, command):
        # Validar o comando
        if command.title == '':
            raise Exception('Nome do usuário é obrigatório.')
        
        if command.description == '':
            raise Exception('E-mail do usuário é obrigatório.')
        
        if command.done == '':
            raise Exception('Senha do usuário é obrigatória.')
        
        # Executar a operação
        # Código para criar um novo usuário no sistema