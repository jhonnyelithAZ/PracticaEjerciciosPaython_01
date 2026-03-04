
largo_cuarto=int(input("escriba el largo del cuarto :"))
ancho_cuarto=int(input("escriba el ancho del cuarto :"))
area=largo_cuarto*ancho_cuarto
if area<12:
    print("caja de fosforo")
elif area>=12 and area<=20:
    print("tas bien")
else:
    print("cule manción compa")