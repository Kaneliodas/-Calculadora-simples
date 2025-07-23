import random
n1 = random.randint(1, 1000)
n2 = random.randint(1, 1000)
print(f"Os números que seram usados são {n1} e {n2}")
sinal = input("Que calculo você gostaria de fazer? +,- ,* ou / ")
if sinal == "+":
    print(n1+n2)
elif sinal == "-":
    print(n1-n2)
elif sinal == "*":
    print(n1*n2)
elif sinal =="/":
    print(n1/n2)
else:
    print("Não existe esse sinal!")