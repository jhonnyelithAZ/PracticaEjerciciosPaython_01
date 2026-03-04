kilometros=int(input("escriba los kilometros recorridos :"))
tiempo=int(input("escriba los minutos que le tomo el viaje :"))
if tiempo<=10:
    print(f"como su viaje demoró {tiempo} minutos,su valor a cobrar es de 5000 pesos")
else:
    print(f"como su viaje demoró {tiempo} minutos,el valor a cobrar es de {kilometros*800} pesos")