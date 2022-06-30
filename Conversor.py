def conversor_pesos(valor_dolar):
  moneda = int(input("Dijite la cantidad de pesos: " ))
  moneda = moneda / valor_dolar
  moneda = round(moneda, 2)
  print(f"Tiene $ {moneda} dolares")

def conversor_dolar(valor_peso):
  moneda = int(input("Dijite la cantidad de dolares: " ))
  moneda = moneda * valor_peso
  moneda = round(moneda, 2)
  print(f"Tiene $ {moneda} pesos")


while True:
  print("""
Bienvenido al sistema para convertir su 💰, por favor elija una de las siguientes opciones:
      
  1. Convertir pesos colombianos a dolares
  2. Convertir pesos mexicanos a dolares
  3. Convertir pesos argentinos a dolares
  4. convertir dolares a pesos colombianos
  5. convertir dolares a pesos mexicanos
  6. convertir dolares a pesos argentinos
  7. salir
      """)
  opcion = int(input ("Seleccione una opcion: "))
  
  #Moneda colombiana a dolares
  if opcion == 1:
    conversor_pesos(4080)
  #Moneda mexicana a dolares
  elif opcion == 2:
    conversor_pesos(20.01)
  #Moneda Argentina a dolares
  elif opcion == 3:
    conversor_pesos(124.11)
  #Dolares a moneda colombiana
  elif opcion == 4:
    conversor_dolar(4080)
  #Dolares a moneda mexicana
  elif opcion == 5:
    conversor_dolar(20.01)
  #Dolares a moneda argentina
  elif opcion == 6:
    conversor_dolar(124.11)
  #salir
  elif opcion == 7:
    print("gracais por usar nuestros servicios, adios")
    break
  #error
  else:
    print("elija solo un numero en la lista")