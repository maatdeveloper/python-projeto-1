from src.interface import InterfaceDoUsuario

class Usuario(InterfaceDoUsuario):
    def __init__(self, nome, email, telefone):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        
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
    
    def cadastrar(self):
        pass
    
    def logar(self):
        pass
    
    def deslogar(self):
        pass
    
    def excluir_conta(self):
        pass
    
    def __str__(self) -> str:
        print(f"""
              Usuário: {self.get_nome}\n
              ===============================\n
              \tEmail: {self.get_email}\n
              \tTelefone: {self.get_telefone}\n
              """)
    
    def __del__(self):
        print(f"Desligando usuário {self.get_nome}")


usuar = Usuario("Matheus", "maat02garcia@gmail.com", "42 999549658")
print(usuar)