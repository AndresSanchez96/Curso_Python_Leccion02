print('Tienda de Libros')
print('Prporciona los siguientes datos del libro: ')
nombre = input('Proporciona el nombre del libro: ')
ID = int(input('Proporciona el ID: '))
precio = float(input('Proporciona el precio: $'))
envio = (input('Indica si el envio es gratuito (True/Flase): ' ))

if envio == 'True':
    envio = True
elif envio == 'False':
    envio = False
else:
    envio = 'Valor incorrecto, debe escribir True o False'

print(f'''
Nombre: {nombre},
ID: {ID},
Precio: {precio},
Envio gratuito? {envio}

''')