INGRESAR_SISTEMA = "1"
OLVIDE_LA_CLAVE = "2"
SALIR = "3"
SEPARADOR = "\n" + "=" * 55 + "\n"

def cajeroAutomatico():
    # Esta es la clave bancaria de Frank, no lo hackeen!!!
    clave = "2503"
    
    intentos = 3
    opcion = 0
    continuar = True

    while(continuar and intentos):
        mostrarOpciones()
        opcion = input("--> Ingrese una opción: ")
        
        if opcion == INGRESAR_SISTEMA:
            claveIngresada = input("\nIngrese su clave bancaria: ")
            # El mensaje esperado, si el ingreso es correcto, debería ser "Bienvenido Frankie-kun"
            if claveIngresada == clave:
                print("Bienvenido Frankie-kun");
                continuar = False;
            else:
                intentos -= 1
                if(intentos > 0):
                    mostrarErrorClaveIncorrecta()
                
        elif opcion == OLVIDE_LA_CLAVE:
            cambiarClave(clave)
        
        elif opcion == SALIR:
            print("\nHasta la próximaaa")
            continuar = False

        else:
            mostrarErrorOpcionInvalida()
        
    if (intentos==0):
        print(SEPARADOR)
        print("xxxx---Cuenta bloqueada por intentos de clave---xxxx");
        print(SEPARADOR)





def mostrarOpciones():
    print("1. Ingresar al sistema")
    print("2. Olvidé la clave")
    print("3. Salir")


# === Implementar ===
def cambiarClave(clave):
    clave = input("Ingrese la nueva clave: ")
    largo = 0
    mensaje = ''
    
    for i in clave:
        largo +=1

    if (clave.isdigit() and largo == 4):
        print(SEPARADOR)    
        mensaje = print("Cambio de clave satisfactorio")
        print(SEPARADOR)  
    else:
        print(SEPARADOR) 
        return print("Digitos no validos")
        print(SEPARADOR) 
    
    
# === Mensajes de error ===
def mostrarErrorClaveIncorrecta():
    print(SEPARADOR)
    print("La clave es incorrecta. Vuelva a intentar.")
    print(SEPARADOR)
    
def mostrarErrorOpcionInvalida():
    print(SEPARADOR)
    print("La opción ingresada no es válida. Vuelva a intentar.")
    print(SEPARADOR)    

# No borrar esta línea
cajeroAutomatico()
