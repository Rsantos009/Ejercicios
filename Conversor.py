while True:
  print("""
Bienvenido al sistema para convertir su dinero, por favor elija una de las siguientes opciones:
      
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
    moneda = int(input("Dijite la cantidad de pesos colombianos: "))
    moneda = moneda / 4080
    moneda = round(moneda, 2)
    print(f"Tiene $ {moneda} dolares")
  #Moneda mexicana a dolares
  elif opcion == 2:
    moneda = float(input("Dijite la cantidad de pesos mexicanos: "))
    moneda = moneda / 20.01
    moneda = round(moneda, 2)
    print(f"Tiene $ {moneda} dolares")
  #Moneda Argentina a dolares
  elif opcion == 3:
    moneda = float(input("Dijite la cantidad de pesos argentinos: "))
    moneda = moneda / 124.11
    moneda = round(moneda, 2)
    print(f"Tiene $ {moneda} dolares")
  #Dolares a moneda colombiana
  elif opcion == 4:
    moneda = float(input("Dijite la cantidad de dolares: "))
    moneda = moneda * 4080
    moneda = round(moneda, 2)
    print(f"Tiene $ {moneda} pesos colombianos")
  #Dolares a moneda mexicana
  elif opcion == 5:
    moneda = float(input("Dijite la cantidad de dolares: "))
    moneda = moneda * 20.01
    moneda = round(moneda, 2)
    print(f"Tiene $ {moneda} pesos mexicanos")
  #Dolares a moneda argentina
  elif opcion == 6:
    moneda = float(input("Dijite la cantidad de dolares: "))
    moneda = moneda * 124.11
    moneda = round(moneda, 2)
    print(f"Tiene $ {moneda} pesos argentinos")
  #salir
  elif opcion == 7:
    print("gracais por usar nuestros servicios, adios")
    break
  #error
  else:
    print("elija solo un numero en la lista")