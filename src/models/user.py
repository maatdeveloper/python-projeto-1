from datetime import datetime as dt
from interface import InterfaceDoUsuario
import sqlite3

conn = sqlite3.connect("user.db")
cursor = conn.cursor()
class Usuario(InterfaceDoUsuario):
    def __init__(self, nome, email, telefone):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.__data_criacao = dt.now().strftime("%d/%m/%Y")
        
        cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (self.__nome, self.__email, self.__telefone, self.__data_criacao))
        conn.commit()
        cursor.close()
        conn.close()
    
    @property
    def get_nome(self):
        return self.__nome
    
    @get_nome.setter
    def set_nome(self, nome):
        self.__nome = nome
        
    @property
    def get_email(self):
        return self.__email
    
    @get_email.setter
    def set_email(self, email):
        self.__email = email
        
    @property
    def get_telefone(self):
        return self.__telefone
    
    @get_telefone.setter
    def set_telefone(self, telefone):
        self.__telefone = telefone
     
    def __str__(self) -> str:
        return f"""
Usuário: {self.get_nome}
===============================
Email:\t\t{self.get_email}
Telefone:\t{self.get_telefone}
Data Criação:\t{self.data_criacao}
              """
    
    def __del__(self):
        print(f"Desligando usuário {self.get_nome}")


usuar = Usuario("Matheus", "exemple@gmail.com", "42 99999-9999")
print(usuar)
