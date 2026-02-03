amount = float(input("Cual es el total de la cuenta? (sin incluir propina) "))
Q = float(input("En un rango del 1-10, ¿Cómo calificarías la CALIDAD de la comida? "))
S = float(input("En un rango del 1-10, ¿Cómo calificarías el SERVICIO? "))
servRatio = float(input("En un rango del 1-10, ¿Que tan importante es el SERVICIO sobre la CALIDAD de la comida? "))

servRatio = servRatio/10
lowTip = 0.05; averTip = 0.15; highTip = 0.25; tipRange = highTip - lowTip
badService = 0; okayService = 3; goodService = 7; greatService = 10; serviceRange = greatService - badService
badFood = 0; okayFood = 6; goodFood = 8; greatFood = 10; foodRange = greatFood - badFood

if S < okayService:
    tip_S = ((averTip - lowTip) / (okayService - badService)) * S + lowTip
elif S < goodService:
    tip_S = averTip
else:
    tip_S = ((highTip - averTip) / (greatService - goodService)) * (S - goodService) + averTip

if Q < okayFood:
    tip_Q = ((averTip - lowTip) / (okayFood - badFood)) * Q + lowTip
elif Q < goodFood:
    tip_Q = averTip
else:
    tip_Q = ((highTip - averTip) / (greatFood - goodFood)) * (Q - goodFood) + averTip

tip = (tip_S * servRatio) + (tip_Q * (1 - servRatio))

print(f"Según tu experiencia, te recomendamos dejar una propina del {tip * 100}%")
print(f"Pagarias un total de: ${amount + (amount * tip):.2f}")