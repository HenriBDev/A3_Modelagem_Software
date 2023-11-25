import sys
from Views.View import View

class MenuView(View):
            
    def menu_inicial(self):
        
        return input(
            "------------Menu Inicial------------\n"
            "O que deseja fazer?\n"
            "1 - Fazer Login\n"
            "2 - Cadastrar usuário\n"
            "3 - Encerrar programa\n"
            "\n"
            "Selecione: "
        )
        
    def menu_principal(self, usuario_logado):
            
        return input(
            "------------ORGANIZADOR DE TAREFAS------------\n"
            f"O que deseja fazer {usuario_logado.nome.capitalize()}?\n"
            "1 - Criar lista\n"
            "2 - Excluir lista\n"
            "3 - Criar tarefa\n"
            "4 - Editar tarefa\n"
            "5 - Executar lista de tarefas\n"
            "6 - Excluir tarefa\n"
            "7 - Checar as listas\n"
            "8 - Trocar de usuário\n"
            "9 - Encerrar programa\n"
            "\n"
            "Selecione: "
        )
        
    def valor_digitado_invalido(self):
        
        return input(
            "Valor digitado inválido!\n"
            "Pressione enter para continuar"
        )
        
    def encerrar_programa(self):
        
        return sys.exit("Encerrando programa...")