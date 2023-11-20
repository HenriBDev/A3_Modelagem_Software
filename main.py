# Python libs
import sys

from Views.TarefaView import TarefaView
from Views.UsuarioView import UsuarioView
from Views.ListaView import ListaView

def main():
    
    usuario_view = UsuarioView()
    lista_view = ListaView()
    tarefa_view = TarefaView()
    
    while True:
        
        while True:
            print("------------Menu Inicial------------\n1 - Fazer Login\n2 - Cadastrar usuário\n3 - Sair")
            valor_digitado = input("O que deseja fazer ?\n")
            if(valor_digitado == '1'):
                usuario_logado = usuario_view.logar_usuario()
                if bool(usuario_logado): break
            elif(valor_digitado == '2'):
                usuario_view.cadastrar_usuario()
            elif(valor_digitado == '3'):
                sys.exit("Programa encerrando...")
            else:
                print('Valor digitado errado') 
    
        while True:
            valor_digitado = input(f"------------ORGANIZADOR DE TAREFAS------------\nO que deseja fazer {usuario_logado.nome}?\n1 - Criar lista?\n2 - Excluir lista?\n3 - Criar tarefa?\n4 - Editar tarefa?\n5 - Concluir tarefa?\n6 - Excluir tarefa\n7 - Checar as listas?\n8 - Trocar de usuário?\n")
            if valor_digitado == '1':
                lista_view.cadastrar_lista(usuario_logado.id)
            elif valor_digitado == '2':
                lista_view.excluir_lista(usuario_logado.id)
            elif valor_digitado == '3':
                id_lista_selecionada = lista_view.selecionar_lista(usuario_logado.id)
                tarefa_view.cadastrar_tarefa(id_lista_selecionada)
            elif valor_digitado == '4':
                id_lista_selecionada = lista_view.selecionar_lista(usuario_logado.id)
                tarefa_view.editar_tarefa(id_lista_selecionada)
            elif valor_digitado == '5':
                id_lista_selecionada = lista_view.selecionar_lista(usuario_logado.id)
                tarefa_view.concluir_tarefa(id_lista_selecionada)
            elif valor_digitado == '6':
                id_lista_selecionada = lista_view.selecionar_lista(usuario_logado.id)
                tarefa_view.excluir_tarefa(id_lista_selecionada)
            elif valor_digitado == '7':
                lista_view.exibir_listas(usuario_logado.id)
            elif valor_digitado == '8': break
            else: print("Valor digitado inválido!")

if __name__ == '__main__':
    main()