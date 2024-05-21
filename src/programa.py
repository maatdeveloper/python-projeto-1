from models.user import Usuario

def menu(nome=""):
    if nome:
        print("*"*50)
        print(f"BEM VINDO {nome}".center(50))
        print("\nEscolha uma opção:")
        print("""\t[a]tualizar
\t[s]air
\t[d]eletar
              """)
        print("➳♥ ", end="")
    
    else:
        print("*"*50)
        print(f"BEM VINDO".center(50))
        print("\nEscolha uma opcão:")
        print("""\t[c]adastro
\t[l]ogin
\t[a]tualizar
\t[s]air
\t[d]eletar
            """)
        print("➳♥ ", end="")


def elefante():
    print("""
   █ 
  █    ███████ 
 ██   ██▓▓███▓██
██   █▓▓▓▓▓▓▓█▓███ 
██  ██▓▓▓   ▓█▓▓█▓█ 
███▓▓▓█▓▓▓▓▓█▓█▓▓▓▓█ 
▀██▓▓█ ██▓▓▓▓██▓▓▓▓▓█ 
 ▀██▀  █▓▓▓▓▓▓▓▓▓▓▓▓▓█ 
        █▓▓▓▓▓█▓▓▓▓▓▓█ 
        █▓▓▓▓█▓█▓▓▓▓▓█ 
        █▓▓▓█▓▓▓█▓▓▓▓█ 
        █▓▓▓█   █▓▓▓█ 
       ██▓██   ██▓▓██
          """)
    

def cadastro(nome, email, telefone):
    user = Usuario(nome, email, telefone)
    return user
