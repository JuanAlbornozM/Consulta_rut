from ast import Try
import os
rut=list()
nombre=list()
edad=list()
nota=list()
alumno=[rut,nombre,edad,nota]
while True:
    os.system('cls')
    print('MENU PRINCIPAL')
    print('1) Agregar Alumno')
    print('2) Consultar por rut')
    print('3) Mostrar todos')
    print('4) Salir')
    op=input('INGRESE OPCION:')
    if op=='1':
        while True:
            try:
                xrut=input('Ingrese rut:')
                xnombre=input('Ingrese nombre:')
                xedad=int(input('Ingrese edad:'))
                xnota=float(input('Ingrese nota:'))
                if xrut.isnumeric() and len(xrut)==8:
                    if len(xnombre)>=3 and len(xnombre)<=100:
                        if xedad>=1 and xedad<=150:
                            if xnota>=1.0 and xnota<=7.0:
                                break;
                input('dato erroneo...')  
            except Exception as e:
                print ('dato incorrecto.....', e)
                input ('pulse una tecla')
        rut.append(xrut)
        nombre.append(xnombre)
        edad.append(xedad)
        nota.append(xnota) 
        input('Datos correctamente ingresados, pulse una tecla para continuar.......')
    elif op=='2':
        try:
            xrut=input('Ingrese rut:')
            i=rut.index(xrut)
            print (f'{alumno[0][i]} {alumno[1][i]} {alumno[2][i]} {alumno[3][i]}')
            input ('pulse una tecla para continuar....')
        except:
            input('rut no existe en lista, se debe ingresar')
    elif op=='3':
        n=len(rut)
        print('LISTA DE ALUMNOS \n ***************************')
        for i in range(n):
            print (f'{alumno[0][i]} {alumno[1][i]} {alumno[2][i]} {alumno[3][i]}')
        input ('pulse una tecla para continuar...............')
    elif op=='4':
        break
    else:
        input('opcion no corresponde, pulse para volver') 