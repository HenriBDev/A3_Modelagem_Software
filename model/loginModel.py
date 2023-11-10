import sqlite3
class loginModel:


    def cadastrar_usuario(usuario):
        con = sqlite3.connect("BD-ListaDeTarefa.db")
        cur = con.cursor() 
        insert = "INSERT INTO Usuario VALUES (?,?,?,?)"
        cur.execute(insert, (usuario.id,usuario.nome, usuario.email, usuario.senha))
        con.commit()
        cur.close()
        return True
    
    def listar_usuario():
        con = sqlite3.connect("BD-ListaDeTarefa.db")
        cur = con.cursor() 
        select = "SELECT * FROM USUARIO"
        cur.execute(select)
        con.commit()
        result = cur.fetchall()        
        cur.close()
        return result

    def login(email,senha):
        con = sqlite3.connect("BD-ListaDeTarefa.db")
        cur = con.cursor() 
        select = "SELECT * FROM USUARIO WHERE email=? AND senha=?"
        cur.execute(select,(email,senha))
        user = cur.fetchone()
        con.commit()
        con.close()
        return user





