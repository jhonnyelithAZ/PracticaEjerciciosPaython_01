nota_1=int(input("anote la primera nota"))
nota_2=int(input("anote la segunda nota"))
nota_3=int(input("anote la segunda nota"))
promedio=(nota_1+nota_2+nota_3)/3
if promedio>=55 and promedio<=59:
    print("usted va a refuerzo pedazo de tibio porque su promedio fue de : ",promedio)
elif promedio<55:
    print("pailas,su promedio fue de :",promedio)
elif promedio>59:
    print("campeon",promedio)
    