class UsuarioService:
    def Criar_Usuario(self, command):
        # Validar o comando
        if command.nome == '':
            raise Exception('Nome do usuário é obrigatório.')
        
        if command.email == '':
            raise Exception('E-mail do usuário é obrigatório.')
        
        if command.senha == '':
            raise Exception('Senha do usuário é obrigatória.')
        
        # Executar a operação
        # Código para criar um novo usuário no sistema