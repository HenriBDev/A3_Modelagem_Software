import sys
import os
from Views.View import View
from Controllers.ControllerFactory import ControllerFactory

class MenuView(View):
    
    def menu_inicial(self):
        
        os.system('cls' if os.name=='nt' else 'clear')
        
        return input(
            "1 - Fazer Login\n"
            "2 - Cadastrar usuário\n"
            "3 - Encerrar programa\n"
            "\n"
            "Selecione: "
        )
        
    def menu_principal(self, id_usuario_logado):
        
        msg_retorno, usuario = ControllerFactory().criar_instancia('usuario').buscar_usuario_por_id(id_usuario_logado)
        
        if msg_retorno != "ok":
            print(msg_retorno)
            return False
        
        os.system('cls' if os.name=='nt' else 'clear')
            
        return input(
            "------------ORGANIZADOR DE TAREFAS------------\n"
            f"Boas vindas {usuario.nome.capitalize()}, o que deseja fazer?\n"
            "1 - Criar lista\n"
            "2 - Excluir lista\n"
            "3 - Criar tarefa\n"
            "4 - Editar tarefa\n"
            "5 - Excluir tarefa\n"
            "6 - Executar lista de tarefas\n"
            "7 - Exibir suas listas e tarefas\n"
            "8 - Trocar de usuário\n"
            "9 - Encerrar programa\n"
            "\n"
            "Selecione: "
        )
        
    @View.view_action
    def valor_digitado_invalido(self):
        print("Valor digitado inválido!")
        
    def encerrar_programa(self):
        
        return sys.exit("Encerrando programa...")