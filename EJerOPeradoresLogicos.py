# valor entre 0 a 5 verificar rangos
valor = int(input('Escribe el valor: '))
valorMinimo = 0
valorMaximo = 5

dentroRango = (valor >= valorMinimo) and (valor <= valorMaximo)

if dentroRango == True:
    print(f'El valor {valor} esta en el rango')
else:
    print(f'El valor {valor} NO esta en el rango')

# Ejercicio de OR

print('Asistir al juego ')
vacaciones = False
diaDescanso = False

if vacaciones or diaDescanso:
    print('Puede asistir al juego')
else:
    print('Tiene deberes por hacer')