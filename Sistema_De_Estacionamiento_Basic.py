from datetime import datetime

print('\n====Bienvenido al sistema de estacionamiento===')

#variables global
regis=[]
informacion_general=[]
espacios_disponibles=[f'{letra}{i}'for letra in 'ABC' for i in range(1,11)]

#creacion de funciones

#agregar datos de la persona
def entrada():
    
    if not espacios_disponibles:
        print('No hay estacionamiento disponible')
        return
    nombre=input('\nIngrese su nombre y apellido (ejm: Lucas Palacio) :\n')
    ced=input('\nIngrese cedula con guiones (ejm: 8-1002-234) : \n')
    tiempo= datetime.now()
    #primer espacio disponible
    puesto=espacios_disponibles.pop(0)
    persona={'Nombre': nombre, 
             'Cedula': ced, 
             'Puesto': puesto,
             'Hora_entrada': tiempo}
    
    regis.append(persona)
    informacion_general.append(persona)
    print(f'registro actual {regis}')
    
    
'''Eliminar datos de la persona al retirarse del estacionamiento
y guardar informacion de salida en la variable (informacion_general)'''
def salida():
    
    nombre=input('\nIngrese su nombre y apellido (ejm: Lucas Palacio) :\n')
    tiempo_sal=datetime.now()
    for name in regis:
        if name['Nombre']==nombre:
            regis.remove(name)
            #liberamos puesto
            espacios_disponibles.append(name['Puesto'])
            espacios_disponibles.sort()
            print('\nVuelva Pronto, ¡buen día\n')
            break
        else: 
            print('\nNo existe en el registro\n')
        
        #calculo para el saldo a pagar y guardar hora de salida en el dict informacion_general
    for persona in informacion_general:
        if persona['Nombre']==nombre:
            hora_entrada= persona['Hora_entrada']
            diferencia = tiempo_sal - hora_entrada
            horas = diferencia.total_seconds() / 3600
            calculo = round(horas * 2, 2)  # $2 por hora
            persona['Hora_Salida']=tiempo_sal
            persona['Saldo a pagar'] = calculo
            print(f'Su saldo a pagar es ${calculo}')
            break
        
#buscar persona en el registro 
def buscar():
    ced=input('Escriba la cedula que desea buscar en el registro: ')
    for persona in regis:
        if persona['Cedula'] ==ced:
            print(persona.items())
            return
    print('No existe en el registro')
    
#Menu principal del programa
while True:

        print('\n==Menu Principal==\n')
        print('1. Buscar persona ')
        print('2. Registrar persona')
        print('3. Marcar Salida')
        print('4. Informacion confidencial')
        print('5. Salir del programa')
        opcion=input('\nIngrese un numero:\n')
        
        if opcion== '1': 
            buscar()
        elif opcion== '2':
            entrada()
        elif opcion == '3':
            salida()
        elif opcion == '4':
            print(informacion_general)
        elif opcion== '5': 
            print('fin del progrma')
            break
        else: 
            print('ingrese una opcion valida')