#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete, así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Un cliente frecuente pide la cantidad de 23 payasos y 54 muñecas, realiza un programa que muestre el peso total de toda la venta.

#Pista: Suponiendo que un cliente pide 5 payasos y 3 muñecas, la juguetería debería hacer la multiplicación de la cantidad de payasos con su peso, al igual que las muñecas; al tener ambos totales de peso, se debe sumar.

#23 Payasos --> 112 g
#54 Munecas --> 75g

# 1 era forma:
CantidadPayasos = 23
CantidadMunecas = 54

Procedimiento = ((CantidadPayasos * 112) + (CantidadMunecas * 75))

print("1-El peso total es de: ",Procedimiento)

# 2 da forma:
print("2-El peso total es de: ", 23 * 112 + 54 * 75)

# 3 ra forma:
CantidadPayasos = 23
CantidadMunecas = 54

Resultado = (CantidadPayasos * 112) + (CantidadMunecas * 75)

print("3-Resultado: " ,Resultado)
