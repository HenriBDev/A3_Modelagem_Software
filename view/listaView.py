class ListaView:
        def exibir_listas(self):
                print(f"Listas de Tarefas:'{lista}'")

        def cadastrar_listas(self):
                lista = input("digite o nome da lista")
                print("Lista cadastrada com sucesso")

        def editar_listas(self):
                lista = input("Qual lista deseja alterar ? (Digite o id dela)")

        def excluir_tarefa(self):
                lista = input("Qual lista deseja excluir ? (Digite o id dela)")
                print("Não é possivel exlcuir lista, pois existe tarefas cadastradas")
                print("Lista excluida com sucesso")