#Cambio de moneda
yuan = int(input("Cuanto tienes de yuan?:"))
yen = int(input("Cuanto tienes de yen?:"))
won = int(input("Cuanto tienes de won?:"))
yuan_dolar = yuan*0.14
yen_dolar = yen*0.0070
won_dolar = won*0.0072
Total = yuan_dolar+yen_dolar+won_dolar

print(Total)