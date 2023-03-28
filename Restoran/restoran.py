
print("Restoranimizga hush kelibsiz!")
m = input('Menyuni ko\'rish uchun "ENTER" tugmasini bosing.')
ichimlik = {"choy":3000,
            "coffee":8000,
            "kompot":15000,
            "moxito":17000,
            "kokteyl":20000
            }

salat = {"olivye":55000,
         "sezar":18000,
         "m_kapriz":35000,
         "fransuzkiy":22000,
         "italyanskiy":25000
         }
ovqat = {"bon dog":55000,
         "hot dog":18000,
         "iskandar":35000,
         "sendvich":22000,
         "lavash":25000
         }
menu1 = [ichimlik, salat, ovqat]
zakaz = []

def drink():
    while True:
        order = input("Qanday ichimlik buyurtma qilasiz? Ichimlik buyurma qilmasangiz \"no\" deb yozing!")
        if order in menu1[0]:
            info = menu1[0]
            inf = info[order]
            zakaz.append(inf)
        elif order == "no":
            break
        else:
            print("Uzur, Bizda bunday ichimlik mavjud emas!!!")
    return order

def salad():
    while True:
        order = input("Qanday salat buyurtma qilasiz? Salat buyurma qilmasangiz \"no\" deb yozing!")
        if order in menu1[1]:
            info = menu1[1]
            inf = info[order]
            zakaz.append(inf)
        elif order == "no":
            break
        else:
            print("Uzur, Bizda bunday salat mavjud emas!!!")
    return order
def meal():
    while True:
        order = input("Qanday ovqat buyurtma qilasiz? Ovqat buyurma qilmasangiz \"no\" deb yozing!")
        if order in menu1[2]:
            info = menu1[2]
            inf = info[order]
            zakaz.append(inf)
        elif order == "no":
            break
        else:
            print("Uzur, Bizda bunday ovqat mavjud emas!!!")
    return order

while True:
    print("Ichimlik \nSalat \nOvqat")
    taom = input("Nima zakaz qilmoqchisiz? Zakaz qilmasangiz \"no\" deb yozing")

    if taom.lower() == 'ichimlik':
        for t, n in menu1[0].items():
            print(f"{t}: {n}")
        drink()
    elif taom.lower() == 'salat':
        for t, n in menu1[1].items():
            print(f"{t}: {n}")
        salad()
    elif taom.lower() == 'ovqat':
        for t, n in menu1[2].items():
            print(f"{t}: {n}")
        meal()
    elif taom == "no":
        break
    else:
        print("Yozishda imlo hatolik yuz berdi!")

print("\n          **          "
      "\n          **          "
      "\n          **          "
      "\n       ********       "
      "\n        ******        "
      "\n         ****         "
      "\n          **          ")
print(f"Siz buyurtirgan taomlarning umumiy summasi {sum(zakaz)} so'm")


