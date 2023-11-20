# Python libs
import sqlite3

class ModelBase:
    
    def conectar_banco(self):
        self.conn = sqlite3.connect("BD-ListaDeTarefa.db")
        self.cursor = self.conn.cursor()
    
    def desconectar_banco(self):
        self.cursor.close()
        self.conn.close()
      
    def executar_query(self, query: str, params: tuple|None = None) -> object:
            
        self.conectar_banco()
            
        if params: self.cursor.execute(query, params)
        else:      self.cursor.execute(query)
        
        comando_query = query.strip().split(' ')[0].lower()
        if comando_query != 'select': self.conn.commit()
        else: result = self.cursor.fetchall()
            
        self.desconectar_banco()
        
        if comando_query == 'select': return result