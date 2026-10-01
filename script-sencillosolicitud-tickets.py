print("SOPORTE EXPRESS")
print("mi nombre es liliana salinas, auxiliar de sopporte N1")

nombre= input("¿como te llamas?")
print("hola", nombre)
area= input ("¿cual es tu area?")
print ("tu area es",area)

print("¡necesitas ayuda de soporte?")
respuesta= input(" responde si o no")


if respuesta.lower() == "si":
    print("haz la solicitud en la app de tickets")
    extension= input ("¿cuales es la extension de tu area?")
    print("pronto llamaremos a la extension", extension, "del area", area)

else:
     print("perfecto, estamos atentos a cualquier solicitud")

