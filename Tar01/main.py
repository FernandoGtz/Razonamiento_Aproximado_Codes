amount = float(input("Cual fue el monto total? "))
quality = int(input("En un rango del 1-10, ¿Cómo calificarías la CALIDAD de la comida? "))
service = int(input("En un rango del 1-10, ¿Cómo calificarías el SERVICIO? "))

tip = 0.01 * (quality + service) + 0.05
amountFinal = amount + (amount * tip)

print(f"Se recomienda dejar una propina del {tip * 100}%")

print(f"Pagarias un total de: ${amountFinal:.2f}")