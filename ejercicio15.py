sueldo_mensual=int(input("escriba el valor de su sueldo mensual :"))
if sueldo_mensual<1500000:
    print("su sueldo sin impuestos es :",sueldo_mensual)
elif sueldo_mensual>1500000 and sueldo_mensual<3000000:
    impuesto=sueldo_mensual*0.05
    print(f"usted debe pagar 5% de impuesto{sueldo_mensual*0.05}porque su salario es de{sueldo_mensual}entonces su sueldo total es de{sueldo_mensual-impuesto}")
else:
   print(f"Usted debe pagar 10% de impuesto {sueldo_mensual*0.10} por que su salario es de {sueldo_mensual} entonces su sueldo total es {sueldo_mensual-sueldo_mensual*0.10}")
