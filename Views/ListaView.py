from Controllers.ListaController import ListaController

class ListaView:
        def exibir_listas(self, usuario_id):
                listas = ListaController().buscar_listas(usuario_id)
                print("Lista de tarefas:")
                for lista in listas:
                        print(f"{lista[0]} - {lista[1]}")
                return [lista[0] for lista in listas]

        def cadastrar_lista(self, usuario_id):
                descricao = input("Digite o nome da lista: ") 
                lista_cadastrada = ListaController().cadastrar_lista(descricao, usuario_id)
                if lista_cadastrada: print("Lista cadastrada com sucesso")

        def excluir_lista(self, usuario_id):
                id_listas = self.exibir_listas(usuario_id)
                id_input = int(input("\nQual lista deseja excluir?\nDigite o número: "))                   
                if(id_input in id_listas):
                        ListaController().excluir_lista(id_input)
                        print('Lista deletada com sucesso')
                else:
                        print("Não há nenhuma lista com esse ID")
                        
        def selecionar_lista(self, usuario_id):
                while True:
                        listas = self.exibir_listas(usuario_id)               
                        lista_id = int(input("Qual lista deseja manipular?\n"))
                        if lista_id in listas:
                                return lista_id
                        else:
                                print("Não há nenhuma lista com esse ID")
