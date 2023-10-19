import openpyxl

# Paso 1 y 2: Solicitar detalles de gastos al usuario
gastos = []

while True:
    fecha = input("Ingrese la fecha del gasto (dd/mm/yyyy) o 'q' para salir: ")
    if fecha.lower() == 'q':
        break
    descripcion = input("Ingrese la descripción del gasto: ")
    monto = float(input("Ingrese el monto del gasto: "))

    gastos.append([fecha, descripcion, monto])

# Paso 3: Guardar los datos en un archivo Excel
informe_gastos = openpyxl.Workbook()
hoja_gastos = informe_gastos.active
hoja_gastos.title = "Gastos"

for gasto in gastos:
    hoja_gastos.append(gasto)

# Paso 4: Calcular total de gastos y resumen
total_gastos = sum(gasto[2] for gasto in gastos)

gasto_mas_caro = max(gastos, key=lambda x: x[2])
gasto_mas_barato = min(gastos, key=lambda x: x[2])

# Paso 5: Imprimir resumen
print(f"Número total de gastos: {len(gastos)}")
print(f"Gasto más caro: Fecha - {gasto_mas_caro[0]}, Descripción - {gasto_mas_caro[1]}, Monto - {gasto_mas_caro[2]}")
print(f"Gasto más barato: Fecha - {gasto_mas_barato[0]}, Descripción - {gasto_mas_barato[1]}, Monto - {gasto_mas_barato[2]}")
print(f"Monto total de gastos: {total_gastos}")

# Paso 6: Guardar el informe en el archivo Excel
informe_gastos.save("informe_gastos.xlsx")

print("El informe de gastos ha sido guardado en 'informe_gastos.xlsx'.")
