#Programa que solicite el año de naciomiento y devuelva la generacion a la que pertenece.and
a= int(input("ingrese su año de nacimiento  "))
if a>=1930 and a<=1949:
    print("usted pertenece a la generacion post-guerra")
if a>1949 and a<=1969:
    print ("usted pertenece a la generacion baby boomer")
if a>1969 and a<=1980:
    print ("usted pertenece a la generacion X")
if a>1980 and a<=1993:
    print ("usted pertenece a la generacion Y")
if a>1993 and a<=2010:
    print ("usted pertenece a la generacion Z")
if a>=2011:
    print ("usted pertenece a la generacion ALFA")