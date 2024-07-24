str="BANANANAAAS"
Stuart=[]
Kevin=[]
long=len(str)
salto=1
vowel=["a","e","i","o","u","A","E","I","O","U"]

while salto<=long:
    for y in range(long):
        pal=str[y:y+salto]
        if len(pal)>=salto:
           print(pal)
           if pal[0] not in vowel:
               Stuart.append(pal)
           else:
               Kevin.append(pal)

    print("------------")
    salto=salto+1
    print(salto)
if len(Stuart)>len(Kevin):
    print("{} {}".format("Stuart", len(Stuart)))
elif len(Stuart)==len(Kevin):
    print("DRAW")
else:
    print("{} {}".format("Kevin", len(Kevin)))

print("fin")


# for x, valor in enumerate(str):
#     longPalabra=x+1
#     for y in range(x,long):
#         pal=str[y:y+longPalabra]
#         print(pal)
#         if pal[0] not in vowel:
#             scot.append(pal)
#     print("-------")
# print(scot)




