import random

usuarios = []
accion = 0
codigo = 0
origen = ''
destino = ''

def viaje () :
  origen = str(input("Ingrese el origen: "))
  destino = str(input("Ingrese el destino: "))
  codigo = round(random.uniform(1, 1000000))
  if origen != '' and destino != '' :
    print(f"El codigo para su viaje de {origen} a {destino} es el {codigo}")
  else :
      print("Ingrese un origen y un destino")  

def login(documento, password):
    usuario = {
        'id': documento,
        'pass': password
    }
    if usuario in usuarios:
        print("Bienvenido")
        viaje()
    else :
        print("Usuario o contraseña incorrectos")
            
            
def registro(documento, password):
    usuarioNuevo = {
        'id': documento,
        'pass': password
    }
    if usuarioNuevo in usuarios:
        print("El usuario ya ha sido creado")
    else :
        print("El usuario se ha creado exitosamente")
        usuarios.append(usuarioNuevo)


while accion!= 3:
    accion = int(input("Ingrese una opcion: \n1. Login \n2. Registro \n3. Salir \n"))
    
    if accion != 3:
        documento = int(input("Ingrese el número de documento: "))
        password = int(input("Ingrese el password: "))
        
    if accion == 1:
        login(documento, password)
        break
    elif accion == 2:
        registro(documento, password)
    elif accion == 3:
        print('Gracias')
        break

