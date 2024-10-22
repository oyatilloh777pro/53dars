# 1-dars

# import math
# from math import sqrt

# son = int(input('Son kiriting: '))
# natija = math.pow(son, 10)
# print(natija)

# 2-dars

# import math
# from math import sqrt

# ism = " oyatilloh "
# familya = " qobiljonov "

# print(ism.upper() + familya.upper())

# 3-dars

# Foydalanuvchidan tug'ilgan yilini so'rash
# tugilgan_yil = int(input("Tug'ilgan yilingizni kiriting: "))

# # Foydalanuvchidan aniqlamoqchi bo'lgan yilini so'rash
# aniqlamoqchi_bolgan_yil = int(input("Yoshingizni aniqlamoqchi bo'lgan yilni kiriting: "))

# # Yoshingizni hisoblash
# if aniqlamoqchi_bolgan_yil >= tugilgan_yil:
#     yosh = aniqlamoqchi_bolgan_yil - tugilgan_yil
#     print(f"Siz {aniqlamoqchi_bolgan_yil} yilda {yosh} yoshda bo'lasiz.")
# else:
#     print("Aniqlamoqchi bo'lgan yil tug'ilgan yildan oldin bo'lishi mumkin emas.")


# 4-dars

# # name = input("Ism kiriting: ")

# # print(name[-1])

# email = input("Email kiriting: ")

# if email.count('@') == 1:
#     if email.endswith('@gmail.com'):
#         if ' ' not in email:
#             print(" To'g'ri keyingi ketma ketlika o'ting! ")
#         else:
#             print('Email ichida bo\' joy bor!')
#     else:
#         print('Email oxirgi @gmail.com bilan tugamagan!')
# else: 
#     print('Email ichida 2 tadan ko\' @ bor!')

# passwoord = input("Parol kiriting: ")
# passwoord1 = input("Parolni tasdiqlang: ")

# if passwoord.count('(!@#$)') == 1 :
#     if len('parol') == 8:


# # son = int(input("Son kiriting: "))

# # if son % 2 ==1:
# #  print("Siz kiritgan son toq son.") 
# # else:
# #  print("Siz kiritgan son juft son.")


# 5-dars

# trub = input(int("To'rtburchakning 1 tomonini kiriting: "))

# trub1 = input(int("To'rtburchakning 2 tomonini kiriting: "))

# trub2 = input(int("To'rtburchakning yuzini kiriting: "))

# if trub == trub1 > trub2:
#  print("Javobi shu:")

# trub = input("Son kiriting kiriting: ")

# if trub == 


# 6-dars
# 1-vazifa

# # for i in range(1, 21):
# #     # print(f"{i} -> Oyatilloh")
# #     # print("Assalomu alaykum")
# #     savat = 1

# #     savat = savat * i
# #     print(savat)

# c = 0

# for i in matn:
#     c += 1

# print(f"{matn} uzunligi {c} ga teng ")



# matn = input(" So'z kiritning: ")
# c = 0
# a = 0

# for i in matn:
#     if in





# 7-dars

# 1-vazifa

# # for i in range(1, 21):
# #     # print(f"{i} -> Oyatilloh")
# #     # print("Assalomu alaykum")
# #     savat = 1

# #     savat = savat * i
# #     print(savat)

# 2-vazifa

# matn = input(" So'z kiritning: ")
# c = 0

# for i in matn:
#     c += 1

# print(f"{matn} uzunligi {c} ga teng ")

# uy ishi

# def unli_undosh_ajrat(soz):
#     unlilar = "aeiou"
#     unli_son = sum(1 for char in soz if char in unlilar)

# if matn == unlilar :
#     print

# 8-dars

# 1-vazifa

# son = int(input("Son kiriting: "))

# for i in range(1, son + 1):
#     print (f"{i} * {i} = {i * i}")

# 2-vazifa


# start = int(input('Son kiriting: '))
# end = int(input('Son kiriting: '))

# for i in range ( start, end + 1):
#  if i % 2 == 0:
#   print(f'{i} --> juft')
#  else:
#   print(f'{i} --> toq')

# 3-vazifa

# 3! = 1,2,3,
# 5! = 1,2,3,4,5
# 10! = 1,2,3,4,5,6,7,8,9,10

# 9-dars
# 1-vazifa

# c = 0
# for i in range(10,75):
#     if i % 2 == 1:
#         c += 1

#         print(c)

# 2-vazifa

# matn = 'salom'

# print(matn[::-1])

# c = 0
# for i in range(10, 200):
    # print(i)
#     if str(i) == str(i)[::-10]:
#         print(i)
#         c +=1
# print()
# print(c)

# 3-vazif

# unli = 0
# undosh = 0

# suz = input("so'z kiriting: ")
# for i in suz:
#     if i in 'aioueAIOUE':
#         unli += 1
# else:
#     undosh += 1

#     print(f'Unli: {unli}\nUndosh: {undosh}')

# 3-vazifa 
# tosh qaychi qog'oz

# import random

# def tosh_qaychi_qogoz():
#     print("Tosh, qaychi, qog'oz o'yiniga xush kelibsiz!")
    
#     # Variantlar ro'yxati
#     variantlar = ["tosh", "qaychi", "qog'oz"]
    
#     # O'yinchidan tanlov so'raymiz
#     user_tanlovi = input("Tanlovingizni kiriting (tosh, qaychi, qog'oz): ").lower()
    
#     # Kompyuter tasodifiy tanlov qiladi
#     komp_tanlovi = random.choice(variantlar)
    
#     print(f"Siz tanladingiz: {user_tanlovi}")
#     print(f"Kompyuter tanladi: {komp_tanlovi}")
    
#     # G'olibni aniqlash qoidalari
#     if user_tanlovi == komp_tanlovi:
#         print("Durang!")
#     elif (user_tanlovi == "tosh" and komp_tanlovi == "qaychi") or \
#          (user_tanlovi == "qaychi" and komp_tanlovi == "qog'oz") or \
#          (user_tanlovi == "qog'oz" and komp_tanlovi == "tosh"):
#         print("Siz g'olib!")
#     else:
#         print("Kompyuter g'olib!")

# # O'yinni boshlaymiz
# tosh_qaychi_qogoz()


# 10-dars
# Bankamat:

# text = """
# 1. Balansni ko'rish
# 2. Naqt pul olish
# 3. Kartani to'ldirish
# 4. Chiqish
# """

# parol = 2525
# balans = 50000


# while True:
#     password = int(input('Parol kiriting: '))

#     if parol == password:
#         print(text)
#         user_input = input("Menyudan birini tanlang: ")

#         if user_input == '1':
#             print()
#             print(f"Sizning balansingiz: {balans}")

#         elif user_input == '2':
#             my_balans = int(input("Boshqa summa: "))
#             if balans > my_balans:
#                 balans = balans - my_balans
#                 print("Pulni oling!")
#             else:
#                 print("Aka biz qarzga ishlamaymiz, qarz munosabatlarni buzadi!")

#         elif user_input == '3':
#             pul = int(input("Mablag' kiriting: "))
#             balans = balans + pul
#             print("OK!")

#         elif user_input == '4':
#             print("Amalyot yakunlandi kartani oling!")
#             break

#     else:
#         print("Parol xato!")

# 11-dars
# List ma'lumot turi
# 1-vazifa
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# print("Birinchi meva: ", mevalar[0])
# print("ikkinchi meva: ", mevalar[1])
# print("to'rtinchi meva: ", mevalar[3])
# print(mevalar[-1])

# 2-vazifa
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# mevalar[2] = 'nok'
# print(mevalar)
  
# 3-vazifa
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# mevalar.append("tarvuz")
# print(mevalar)


# mashinalar = []

# for i in range(1, 6):
#  mashina = input(" Kalektsyangizga 1-chi mashinani kiriting: ")
#  mashinalar.append(mashina)

# print(mashinalar)

# 12-dars
# 1-vazifa

# cars = ['bmw', 'maclaren', 'pagani']
# cars.insert(1, 'ferrari')
# print(cars)

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor' ]
# print(mevalar)
# del mevalar[2]
# print(mevalar)

# mevalar = ['olma', 'anjir', 'shaftoli', 'o\'rik', 'anor']
# mevalar.remove('olma')
# print(mevalar)

# hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
# hayvonlar.remove("mushuk")
# print(hayvonlar)

# 13-dars
# 1-vazifa

# dostlar = ["ali", "vali", "doston", "ulug'bek", "abdulloh"]
# dostlar.sort()
# print(dostlar)

# 2-vazifa

# l1 = [1, 5, 7, 15]
# l2 = [3, 4, 5]

# # 1-usul
# l1 += l2

# # 2-usul
# for i in l2:
#     l1.append(i)
    
# print(l1)   

# 13-dars
# 1-vazifa

# l = [1, 2, 3, 8, 7, 10]
# s = 0
# for i in l:
#     s += i

# print(s)

# print(sum(l))


# l = [1, 2, 3, 8, 7, 10]

# print(max(l) - min(l))

# 2-vazifa

# toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])

# 3-vazifa

# toys = ('bus','car','bear','dino','snake','lizard')
# toys = list(toys)
# toys[3] = 'dragon'
# toys = tuple(toys)
# print(toys)

# uy ishi
# 1-vazifa

# t = (4, 1, 8, 7)

# print(max(t))
# print(min(t))

# 2-vazifa

# t = (4, 1, 8, 7)

# print(sorted(t))

# # 3-vazifa

# t = (4, 1, 8, 7)

# print(sorted(t,reverse=True))

# 4-vazifa

# t = (4, 1, 8, 7)

# juft = 0
# toq = 0
 
# for i in t:
#     if i % 2 == 0:
#         juft += i
#     else:
#         toq += i
# print(juft)
# print(toq)

# 14-dars
# 1-vazifa

# t = (1, 5, 7, 8)

# print(t.count(5))
# print(t.index(5))

# 2-vazifa

# inson = {
#      'ism':'Oyatilloh',
#      'familya':'Qobiljonov',
#      'yosh':13,
#      'manzil':{
#       'tuman': 'sag\'bon',
#       'mahalla':{
#         'ko\'cha': 'qorasaroy',
#         'uy': 7/60
#         }
#     } 
#         }

# print(inson['age'])

# print(f"Foydalanuvchi ismi: {inson['ism']}")
# print(f"Foydalanuvchi yoshi: {inson['yosh']}")
# print(f"Foydalanuvchi familyasi: {inson['familya']}")
# print(f"Foydalanuvchi tumani: {inson['manzil']['tuman']}")
# print(f"Foydalanuvchi kucha: {inson['manzil']['mahalla']['kucha']}")
# print(f"Foydalanuvchi uyi: {inson['manzil']['mahalla']['uy']}")

# uy ishi

# # Mevalar nomli dict yaratamiz
# mevalar = {}

# # Foydalanuvchidan 5 ta meva nomi va narxini kiritishini so'raymiz
# for i in range(5):
#     nomi = input(f"{i+1}-meva nomini kiriting: ")
#     narxi = int(input(f"{i+1}-meva narxini kiriting: "))
#     mevalar[nomi] = narxi

# # Natijani chop etamiz
# print(mevalar)



# 15-dars
# 1-vazifa

# mevalar = {}

# for i in range(1, 6):
#  name = input("Meva nomini kiriting: ")
# price = int(input("Meva narxini kiriting: "))
# mevalar[name] = price
# print(mevalar)


# mevalar = {
#     'olma': 12000,
#     'banan': 25000,
#     'shaftoli': 18000,
#     'uzum': 15000
# }

# meva = input("Meva nomini kiriting: ")

# for i in mevalar:
#     if i == meva.lower():
#         print(f'{meva.title()} ning narxi: {mevalar[i]}')
#         break
#     else:
#         print("Bizda bunday meva qolmagan!")
#         break


# 16-dars
# 1-vazifa

# telefonlar = {
#     'ali':'iphone x',
#     'sobir':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
# }

# telefon = telefonlar.get('vali', "Bunday isimli odam yo'q!")
# print(telefon)


# talaba = {'ism':'Murod Olimov', 'yosh':24,'t__yil':2000}
# print(talaba)
# del talaba['yosh']
# print(talaba)

# 2-vazifa
# l = [1, 2, 3]

# if len(l) == len(set(l)):
#     print(True)
# else:
#     print(False)

# 17-dars
# 1-vazifa

# def salom__ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu aleykum!")

# salom__ber()

# 2-vazifa 


# def salom__ber(ism: str):
#     """Foydalanuvchi ismini qabul qilib, unga salom beruvchi funksiya"""
#     print(f"Assalomu aleykum, hurmatli {ism.title()}!")

# salom__ber(ali)

# 3-vazifa

# def full__name(first_name, last_name):
#     print(f"Foydalanuvchining to'liq ism familyasi {first_name} {last_name}")

# name = input("Ism kiriting: ")
# familya = input("Familya kiriting: ")    

# full__name(name, familya)

# 3-vazifa

# def full_nambir(son_nambir, qoshiuvchi_nambir):
#     print(f"Foydalanuvchining kiritgan soning yig'indisi {son_nambir} {qoshiuvchi_nambir}")

# name = input("Son kiriting: ")
# familya = input("Qo'shiluvchi sonni kiriting: ")    

# full_nambir(name, familya)

# 18-dars
# 1-vazifa

# def summa(a, b):
#     print(f'a = {a}')
#     print(f'b = {b}')
#     # print(a + b)

# summa(5, 3)
# print()
# summa(b=3, a=5)

# summa(5, b=3)

# 2-vazifa
# ism = input("Ismingizni kiriting: ")
# yosh = int(input("Yoshingizni kiriting: "))

# def yosh_hisobla(kirit_yil):
#     hoz_yil = 2024
#     tugilgan = hoz_yil - kirit_yil
#     return tugilgan

# tugilgan = yosh_hisobla(yosh)
# print(f"{ism} sizning tug'ilgan yilingiz {tugilgan}.")
