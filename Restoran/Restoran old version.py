print("Restoranimizga hush kelibsiz!")
print("Quyidagi menu bo'yicha taom tanlashingiz mumkin")
menu = {"choy":3000,
            "coffee":8000,
            "kompot":15000,
            "moxito":17000,
            "kokteyl":20000,
            "olivye":55000,
            "sezar":18000,
            "bon dog":55000,
            "hot dog":18000,
            "iskandar":35000,
            "sendvich":22000,
            "lavash":25000
            }

for t, n in menu.items():
    print(f"{t}: {n}")
order = []
while True:
    taom = input("Taom nomini kiriting: ").lower()
    if taom in menu:
        info = menu[taom]
        order.append(info)
    else:
        print("Bizda bunday taom mavjud emas")
    javob = input("yana taom kiritasizmi? ha/yo'q")
    if javob == "ha":
        continue
    else:
        break

print(sum(order))