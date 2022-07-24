"""
Created on Wed July 16  18:20:15 2022

@Aftor: Ilhomjon
"""

#1.vazifa

#son = float(input("Juft son kiriting : "))
#if son % 2 == 0:
#    print('Rahmat!')
#else:
#    print("Bu son juft emas!")

#2.vazifa

#yosh = int(input("Yoshingiz nechida ? \n Yosh = "))
#if yosh <= 4 or yosh >= 60:
#    print('Kirish bepul!')
#elif yosh <= 18:
#    print('Kirish 10000 so`m')
#else:
#    print('Kirish 20000 so`m')

#3.vazifa

#print('Ikkita son kiriting >>>')
#x = float(input("Birinchi sonni kiriting : "))
#y = float(input("Ikkinchi sonni kiriting : "))
#if x == y:
#    print(f"{x} = {y}")
#elif x > y:
#    print(f"{x} > {y}")
#else: 
#    print(f"{x} < {y}")

#4.vazifa

#mahsulotlar = ['nok', 'anor', 'uzum', 'un', 'gilos', 'behi', 'non', 'shakar', 'tuz', 'yog']
#savat = []
#for n in range(5):
#    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
#for tovar in savat:
#    if tovar in mahsulotlar:
#        print(f"Do`konimizda {tovar} bor")
#    else:
#        print(f"Do`konimizda {tovar} yo`q")

#5.vazifa

#mahsulotlar = ['nok', 'anor', 'uzum', 'un', 'gilos', 'behi', 'non', 'shakar', 'tuz', 'yog']
#savat = []
#for n in range(5):
#    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

#mavjud = []
#mavjudmas = []

#for tovar in savat:
#    if tovar in mahsulotlar:
#        mavjud.append(tovar)
#    else:
#        mavjudmas.append(tovar)

#if mavjudmas:        
#    print(f"Do`konimizda quyidagi mahsulotlar yo`q :")
#    for tovar in mavjudmas:
#        print(tovar)
#else:
#    print('Siz so`ragan barcha mahsulotlar do`konimizda bor')

#6.vazifa

#foydalanuvchi = ['anvar', 'begzod', 'umar', 'sherzod', 'ilhom']
#login = input("Yangi login tanlang: ")
#if login in foydalanuvchi:
#    print('Login band, iltimos boshqa login tanlang!')
#else:
#    print(f"Salom {login.capitalize()} \nXush kelibsiz!")

#7.vazifa

#son = int(input("Istalgan butun son kiriting : "))
#for n in range(2,11):
#    if not son%n :
#        print(f"{son} soni {n} ga qoldiqsiz bo`linadi")