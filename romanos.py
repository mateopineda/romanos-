import math  
Unidades=["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]  
Decenas=["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]  
Centenas=["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]  
for numero in range(1,1001):
    if(numero==1000):
        print("M")    
    else:    
        if(numero>=100):
            unidad= numero % 10  
            decena=int(math.floor(numero/10))%10  
            centena=int(math.floor(numero/100))  
            print(Centenas[centena]+Decenas[decena]+Unidades[unidad])  
        else:  
            if(numero>=10):
                unidad= numero % 10  
                decena=int(math.floor(numero/10))%10  
                print(Decenas[decena]+Unidades[unidad])  
            else:
                unidad= numero % 10  
                print(Unidades[numero])  
