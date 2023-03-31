class CriarUsuarioCommand:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.done = False