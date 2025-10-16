class Usuario_cadastrado:
    def __init__(self):
        self._usuarios = [
            {"nome": "Samuel", "nivel": 3},
            {"nome": "Alex", "nivel": 2},
            {"nome": "Cristian", "nivel": 1}
        ]

    def get_usuario_nome(self, nome):
        
        for usuario in self._usuarios:
            # .strip() remove espaços em branco do início e do fim
            if usuario['nome'].strip().lower() == nome.strip().lower():
                return usuario
        return None