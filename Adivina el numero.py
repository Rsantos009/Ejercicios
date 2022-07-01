import random

def run():
  vidas = 5
  numero_aleatorio = random.randint(1, 100)
  print (f"tienes {vidas} vidas\n")
  numero_elegido = int(input("Elige un numero del 1 al 100: \n"))
  while numero_elegido != numero_aleatorio:
    if numero_elegido < numero_aleatorio:
      print("Busca un numero mas grande\n")
      vidas = vidas -1
      print(f"Te quedan {vidas} vidas\n")
    if numero_elegido > numero_aleatorio:
      print("Busca un numero mas pequeño\n")
      vidas = vidas - 1
      print(f"Te quedan {vidas} vidas\n")
    if vidas == 0:
      print ("te quedaste sin vidas, PERDISTE\n")
      print (f"El numero era {numero_aleatorio}")
      break
    numero_elegido = int(input("Elige otro numero: \n"))
    if numero_elegido == numero_aleatorio:
      print("GANASTE")

if __name__ == "__main__":
  run()