from Views.View import View

class UsuarioView(View): 
    
    @View.view_action
    def logar_usuario(self) -> object|bool:

        print("Logando usuário")
        email = input("Digite seu e-mail: ")
        senha = input("Digite sua senha: ")
        msg_retorno, retorno = self.controller.logar_usuario(email, senha)
        print("\nUsuário logado com sucesso!" if msg_retorno == "ok" else msg_retorno)
        return retorno
        
    @View.view_action
    def cadastrar_usuario(self) -> bool:

        print("Cadastrando usuário")
        novo_email = input("Digite o seu e-mail: ")
        novo_nome = input("Digite o seu nome: ")
        nova_senha = input("Digite a sua senha: ")
        msg_retorno = self.controller.cadastrar_usuario(novo_email, nova_senha, novo_nome)
        print("Usuário cadastrado com sucesso!" if msg_retorno == "ok" else msg_retorno)
                