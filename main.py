import random

usuarios = []
prestamosUsuarios = []
bicicletas = ["false", "true", "false", "false"]
accion = 0
numeroTarjeta = 0
origen = ''
destino = ''

def viaje (numeroTarjeta) :
    tarjeta = int(input('Ingreso el numero tarjeta: '))
    origen = str(input("Ingrese el origen: "))
    destino = str(input("Ingrese el destino: "))
    if origen != '' and destino != '' and tarjeta == numeroTarjeta :
        if 'true' in bicicletas :
            prestamosUsuarios.append({'origen': origen, 'destino': destino})
            print(f"Reserva exitosa")
        else :
            print(f"No hay bicicletas disponibles")
    else :
        print(f"Ingrese un origen y un destino y verifique el número de tarjeta") 


def menuLogin(tarjeta) :
    accionesLogin = 0
    accionesLogin = int(input("Ingrese una opcion: \n1. Consultar usuarios \n2. Consultar prestamos \n3. Prestar bicicleta  \n4. Salir "))
    while accionesLogin != 4 :
        if accionesLogin == 1 :
            for usuario in usuarios :
                print(usuario)
                break
        elif accionesLogin == 2 :
            for prestamo in prestamosUsuarios :
                print(prestamo)
        elif accionesLogin == 3 :
            viaje(tarjeta)
        elif accionesLogin == 4 :
            print('Gracias')
            break  
                   

def login(documento, password):
    usuario = {
        'id': documento,
        'pass': password
    }
    for usuario in usuarios :
        if usuario['id'] == documento and usuario['pass'] == password:
            print("Bienvenido")
            menuLogin(usuario['numeroTarjeta'])
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
        tarjeta  = round(random.uniform(1, 100))
        usuarioNuevo = {
            'id': documento,
            'pass': password,
            'numeroTarjeta': tarjeta
        }
        usuarios.append(usuarioNuevo)
        print(f"El usuario se ha creado exitosamente, su tarjeta es la {tarjeta}")


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

