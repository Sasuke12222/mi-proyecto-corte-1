# Infraestructura TI
# Calcular forma de pago de sus ordenes de compra.

pieza_a_comprar = input("que pieza se va a comprar: ")
numero_de_piezas = int(input(f"cantidad de {pieza_a_comprar} que desea comprar: "))
precio_unitario = float(input(f"ingrse el precio por UNIDAD de {pieza_a_comprar.upper()}: "))


monto_total = numero_de_piezas * precio_unitario


if monto_total > 500000:
    dinero_empresa = monto_total * 0.55
    prestamo_banco = monto_total * 0.30
    credito_solicitado = monto_total * 0.15
    interes = credito_solicitado * 0.20
    total_interes = interes + credito_solicitado
else:
    dinero_empresa = monto_total * 0.70
    prestamo_banco = 0
    credito_solicitado = monto_total * 0.30
    interes = credito_solicitado * 0.20
    total_interes = interes + credito_solicitado


print("\n")
print(f"se compraran", numero_de_piezas, pieza_a_comprar )
print(f"el precio por cada", pieza_a_comprar, "es de", int(precio_unitario))
print("el monto total de la compra es de ",int(monto_total))
print(f"La inversion de la empresa es ", int(dinero_empresa) )
print(f"el credito solicitado más intereses es de ", int(total_interes) )
print(f"el prestamo al banco es de ", prestamo_banco)