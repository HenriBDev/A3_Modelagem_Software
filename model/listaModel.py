import sqlite3
class ListaModel():

    def cadastrar_lista(lista):
        try:
            con = sqlite3.connect("BD-ListaDeTarefa.db")
            cur = con.cursor()
            insert= "INSERT INTO LISTA VALUES(?,?,?);"        
            cur.execute(insert,(lista.id,lista.descricao,lista.usuario_id)) 
            con.commit()
            cur.close()
        except Exception as e:
            print(f"Erro ao cadastrar lista: {str(e)}")

    def editar_lista(lista):
        try:
            con = sqlite3.connect("BD-ListaDeTarefa.db")
            cur = con.cursor()
            update= "UPDATE LISTA set descricao=? WHERE id=?;"        
            cur.execute(update,(lista.descricao,lista.id)) 
            con.commit()
            cur.close()
        except Exception as e:
            print(f"Erro ao editar lista: {str(e)}")

    def excluir_lista(lista):
        try:
            con = sqlite3.connect("BD-ListaDeTarefa.db")
            cur = con.cursor()
            insert= "DELETE FROM LISTA WHERE id=?;"        
            cur.execute(insert,(lista.id)) 
            con.commit()
            cur.close()
        except Exception as e:
            print(f"Erro ao excluir lista: {str(e)}")