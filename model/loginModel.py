import sqlite3
class loginModel:


    def cadastrar_usuario(usuario):
        try:
            con = sqlite3.connect("BD-ListaDeTarefa.db")
            cur = con.cursor() 
            insert = "INSERT INTO Usuario VALUES (?,?,?,?)"
            cur.execute(insert, (usuario.id,usuario.nome, usuario.email, usuario.senha))
            con.commit()
            cur.close()
            return True
        except Exception as e:
            print(f"Erro ao cadastrar usuário: {str(e)}")
    
    def listar_usuario():
        try:
            con = sqlite3.connect("BD-ListaDeTarefa.db")
            cur = con.cursor() 
            select = "SELECT * FROM USUARIO"
            cur.execute(select)
            con.commit()
            result = cur.fetchall()        
            cur.close()
            return result
        except Exception as e:
            print(f"Erro ao listar usuário: {str(e)}")

    def login(email,senha):
        try:
            con = sqlite3.connect("BD-ListaDeTarefa.db")
            cur = con.cursor() 
            select = "SELECT * FROM USUARIO WHERE email=? AND senha=?"
            cur.execute(select,(email,senha))
            user = cur.fetchone()
            con.commit()
            con.close()
            return user
        except Exception as e:
            print(f"Erro ao fazer login: {str(e)}")





