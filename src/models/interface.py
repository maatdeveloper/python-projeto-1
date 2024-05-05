from abc import ABC, abstractmethod

class InterfaceDoUsuario(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def logar(self):
        pass
    
    @abstractmethod
    def deslogar(self):
        pass
    
    @abstractmethod
    def __del__(self):
        pass