import sqlite3
class TarefaModel:

    def cadastrar_tarefa(tarefa):
        try:
            con = sqlite3.connect("BD-ListaDeTarefa.db")
            cur = con.cursor()
            insert= "INSERT INTO TAREFA VALUES(?,?,?,?,?);"        
            cur.execute(insert,(tarefa.id,tarefa.descricao,tarefa.status,tarefa.tempo,tarefa.lista_id))
            con.commit()
            cur.close()
            con.close()
        except Exception as e:
            print(f"Erro ao cadastrar tarefa: {str(e)}")

    def editar_tarefa(tarefa):
        try:
            con = sqlite3.connect("BD-ListaDeTarefa.db")
            cur = con.cursor()
            update= "UPDATE TAREFA set descricao=?, concluida=?, tempo=? WHERE id=?;"        
            cur.execute(update,(tarefa.descricao,tarefa.status,tarefa.tempo, tarefa.id)) 
            con.commit()
            cur.close()
            con.close()
        except Exception as e:
            print(f"Erro ao editar tarefa: {str(e)}")

    def concluir_tarefa(tarefa_id):
        try:
            con = sqlite3.connect("BD-ListaDeTarefa.db")
            cur = con.cursor()
            update= "UPDATE TAREFA set concluida=1 WHERE id=?;"        
            cur.execute(update,(tarefa_id)) 
            con.commit()
            cur.close()
            con.close()
        except Exception as e:
            print(f"Erro ao concluir tarefa: {str(e)}")
    
    def excluir_tarefa(tarefa_id):
        try:
            con = sqlite3.connect("BD-ListaDeTarefa.db")
            cur = con.cursor()
            delete= "DELETE FROM TAREFA WHERE id=?;"        
            cur.execute(delete,(tarefa_id)) 
            con.commit()
            cur.close()
            con.close()
        except Exception as e:
            print(f"Erro ao excluir tarefa: {str(e)}")

    def exibir_tarefas(lista_id):
        try:
            con = sqlite3.connect("BD-ListaDeTarefa.db")
            cur = con.cursor()
            select= f"SELECT * FROM TAREFA WHERE lista_id={lista_id};"        
            cur.execute(select)
            result = cur.fetchall() 
            con.commit()
            cur.close()
            con.close()
            return  result
        except Exception as e:
            print(f"Erro ao excluir tarefa: {str(e)}")    
    
    def verificar_tarefas_na_lista(lista_id):
        try:
            con = sqlite3.connect("BD-ListaDeTarefa.db")
            cur = con.cursor()
            select= f"SELECT * FROM TAREFA WHERE lista_id={lista_id}"        
            cur.execute(select)
            tarefas = cur.fetchall()
            con.commit()
            cur.close()
            con.close()
            return tarefas
        except Exception as e:
            print(f"Erro ao listar lista: {str(e)}")
