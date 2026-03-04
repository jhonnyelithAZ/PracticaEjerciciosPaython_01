edad=int(input("escriba su edad :"))
estrato=int(input("escriba su estrato :"))

if (edad>=18 and edad<=25) and (estrato==1 or estrato==2 or estrato==3):
    print("aplica subsidio")

else:
    print("no aplica subsidio")




