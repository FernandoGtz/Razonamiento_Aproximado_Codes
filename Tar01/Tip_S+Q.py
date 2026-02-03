amount = float(input("Cual es el total de la cuenta? (sin incluir propina) "))
Q = float(input("En un rango del 1-10, ¿Cómo calificarías la CALIDAD de la comida? "))
S = float(input("En un rango del 1-10, ¿Cómo calificarías el SERVICIO? "))
servRatio = float(input("En un rango del 1-10, ¿Que tan importante es el SERVICIO sobre la CALIDAD de la comida? "))

servRatio = servRatio/10
lowTip = 0.05; averTip = 0.15; highTip = 0.25; tipRange = highTip - lowTip
badService = 0; okayService = 3; goodService = 7; greatService = 10; serviceRange = greatService - badService
badFood = 0; greatFood = 10; foodRange = greatFood - badFood

if (S<okayService):
    tip = (((averTip - lowTip) / (okayService - badService)) * S + lowTip) * servRatio + (1 - servRatio) * (tipRange / foodRange * Q + lowTip)
elif (S<goodService):
    tip = averTip * servRatio + (1-servRatio) * (tipRange / foodRange * Q + lowTip)
else :
    tip = (((highTip-averTip) / (greatService-goodService)) * (S-goodService) + averTip) * servRatio + (1 - servRatio) * (tipRange / foodRange * Q + lowTip)

print(f"Según tu experiencia, te recomendamos dejar una propina del {tip * 100:.0}%")
print(f"Pagarias un total de: ${amount + (amount * tip):.2f}")