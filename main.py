# ejemplo de estaciones

monht = input('Digite el mes del año: ').lower()
if(monht == "diciembre" or monht =="enero" or monht =="febrero" or monht =="marzo"):
    print("Estas en invierno")
elif(monht =="abril" or monht =="mayo"):
        print("Estas en primavera")
elif(monht == "junio" or monht =="julio" or monht =="agosto"):
        print("Estas en verano")
elif(monht == "septiembre" or monht =="octubre" or monht == "noviembre"):
    print("Estas en otoño")
else:
    print("No has digitado un mes valido")



