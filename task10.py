n = int(input('Введите количество монет '))

orel = 0
reshka = 0

for i in range(n):
    x = int(input())
    
    if x == 1:
        orel += 1
    else:
        reshka += 1

if orel < reshka:
    print(f'Переверните {orel} монет с орла на решку')

elif orel == reshka:
    print(f'Количество орлов и решек одинаково')

else:
    print((f'Переверните {reshka} монет с решки на орла'))