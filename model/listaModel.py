import sqlite3
class ListaModel():

    def cadastrar_lista(lista):
        con = sqlite3.connect("BD-ListaDeTarefa.db")
        cur = con.cursor()
        insert= "INSERT INTO LISTA VALUES(?,?,?);"        
        cur.execute(insert,(lista.id,lista.descricao,lista.usuario_id)) 
        con.commit()
        cur.close()

    def editar_lista(lista):
        con = sqlite3.connect("BD-ListaDeTarefa.db")
        cur = con.cursor()
        update= "UPDATE LISTA set descricao=? WHERE id=?;"        
        cur.execute(update,(lista.descricao,lista.id)) 
        con.commit()
        cur.close()

    def excluir_lista(lista):
        con = sqlite3.connect("BD-ListaDeTarefa.db")
        cur = con.cursor()
        insert= "DELETE FROM LISTA WHERE id=?;"        
        cur.execute(insert,(lista.id)) 
        con.commit()
        cur.close()