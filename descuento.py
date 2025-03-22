# Función para calcular descuento
def calcular_descuento(compra_total, porcentaje_del_descuento=10):
    descuento1 = compra_total * (porcentaje_del_descuento / 100)
    return descuento1
#primer programa
# Solicitar al usuario el monto total de la compra
valor_a_pagar = float(input("Ingresa el monto total de la compra: "))
# Calcular el descuento usando el valor predeterminado del 10%
descuento2 = calcular_descuento(valor_a_pagar)
print("Descuento para la compra de", valor_a_pagar, "es:", descuento2)
#segundo programa
# Solicitar al usuario otro monto total de la compra y el porcentaje de descuento
valor_total_apagar = float(input("Ingresa otro monto total de la compra: "))
porcentaje_descuento2 = float(input("Ingresa el porcentaje de descuento: "))
# Calcular el descuento con el porcentaje dicho por el usuario
descuento2 = calcular_descuento(valor_total_apagar, porcentaje_descuento2)
print("Descuento para la compra de", valor_total_apagar, "con un descuento del", 
porcentaje_descuento2, "% es:", descuento2)
