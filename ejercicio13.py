precio_producto=int(input("coloque el precio del producto :"))

if precio_producto>=100000:
    descuento=100000*0.10
    print("el precio con descuento es:",precio_producto-descuento)


else:
    print("el precio de su producto es",precio_producto)
     