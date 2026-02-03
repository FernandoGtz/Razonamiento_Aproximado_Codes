amount = float(input("Cual es el total de la cuenta? (sin incluir propina) "))
S = int(input("En un rango del 1-10, ¿Cómo calificarías el SERVICIO? "))

tip = 0.20 / 10 * S + 0.05

amountFinal = amount + (amount * tip)
print(f"Según tu experiencia, te recomendamos dejar una propina del {tip * 100}%")
print(f"Pagarias un total de: ${amountFinal:.2f}")