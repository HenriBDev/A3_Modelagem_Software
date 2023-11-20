# Python libs
import sys

from Views.TarefaView import TarefaView
from Views.UsuarioView import UsuarioView
from Views.ListaView import ListaView

def main():
    
    usuario_view = UsuarioView()
    lista_view = ListaView()
    
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
            valorDigitado = input(f"------------ORGANIZADOR DE TAREFAS------------\nO que deseja fazer {usuario_logado.nome}?\n1 - Criar uma lista de tarefas nova?\n2 - Excluir alguma lista já existente?\n3 - Remover tarefas de alguma lista?\n4 - Checar as listas?\n5 - Trocar de usuário?\n")
            if(valorDigitado == '1'):
                lista_view.cadastrar_lista(usuario_logado.id)
            elif(valorDigitado == '2'):
                lista_view.excluir_lista(usuario_logado.id)
            elif(valorDigitado == '3'):
                TarefaView().excluir_tarefa()
            elif(valorDigitado == '4'):
                lista_view.exibir_listas(usuario_logado.id)
            elif(valorDigitado == '5'): break
            else: print("Valor digitado inválido!")

if __name__ == '__main__':
    main()