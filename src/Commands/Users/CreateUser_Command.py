class CriarUsuarioCommand:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.done = False

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "done": self.done
        }