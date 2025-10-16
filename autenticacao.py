from dados_usuarios import Usuario_cadastrado

class Autenticacao:
    def __init__(self):
        self.usuario_cadastrado = Usuario_cadastrado()

    def autenticar(self, nome, nivel):
        """
        Verifica se o usuário existe e se seu nível é suficiente.
        """
        usuario = self.usuario_cadastrado.get_usuario_nome(nome)
        
        if not usuario:
            return "Usuario Desconhecido"
            
        if usuario['nivel'] >= nivel:
            return "Acesso Concedido"
        else:
            return f"Acesso Negado. Nivel insuficiente: {usuario['nivel']}"

