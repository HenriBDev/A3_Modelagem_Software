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
            con.close()
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
            con.close()
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
            con.close()
        except Exception as e:
            print(f"Erro ao excluir lista: {str(e)}")
            
    def listar_listas(listar_user_id):
        try:
            con = sqlite3.connect("BD-ListaDeTarefa.db")
            cur = con.cursor()
            insert= f"SELECT * FROM LISTA WHERE usuario id = {listar_user_id}"
            result = cur.execute(insert)
            cur.close()
            con.close()
            return result
        except Exception as e:
            print(f"Erro ao excluir lista: {str(e)}")
