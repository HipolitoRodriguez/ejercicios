
import math
x = {'a': 1, 'b': 2, 'c': 3}

print(*x.values())

cateto1=float(input())
cateto2=float(input())
hiptenusa=(math.sqrt(cateto1**2+cateto2**2))/2
res=math.asin(hiptenusa/cateto2)
angulo=round(math.degrees(res)+.00000001)
print("{}{}".format(angulo,chr(176)))

# Obtener el area del cuadro #
area=cateto1*cateto2
print(area)
print("hola mundo cruel, estoy de suerte")
print("mas prints")
print("se hace desded la linea de comandos, las variables")

# fin
