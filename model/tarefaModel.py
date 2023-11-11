import sqlite3
class TarefaModel:

    def cadastrar_tarefa(tarefa):
        con = sqlite3.connect("BD-ListaDeTarefa.db")
        cur = con.cursor()
        insert= "INSERT INTO TAREFA VALUES(?,?,?,?,?);"        
        cur.execute(insert,(tarefa.id,tarefa.descricao,tarefa.status,tarefa.tempo,tarefa.lista_id)) 
        con.commit()
        cur.close()

    def editar_tarefa(tarefa):
        con = sqlite3.connect("BD-ListaDeTarefa.db")
        cur = con.cursor()
        update= "UPDATE TAREFA set descricao=?, concluida=?, tempo=? WHERE id=?;"        
        cur.execute(update,(tarefa.descricao,tarefa.status,tarefa.tempo, tarefa.id)) 
        con.commit()
        cur.close()

    def concluir_tarefa(tarefa):
        con = sqlite3.connect("BD-ListaDeTarefa.db")
        cur = con.cursor()
        update= "UPDATE TAREFA set concluida=? WHERE id=?;"        
        cur.execute(update,(tarefa.status, tarefa.id)) 
        con.commit()
        cur.close()
    
    def excluir_tarefa(tarefa):
        con = sqlite3.connect("BD-ListaDeTarefa.db")
        cur = con.cursor()
        delete= "DELETE FROM TAREFA WHERE id=?;"        
        cur.execute(delete,(tarefa.id)) 
        con.commit()
        cur.close()
