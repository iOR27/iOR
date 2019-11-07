def calculateBMI():
    height = float(input("Введите свой рост: "))
    weight = float(input("Введите свой вес: "))

    return weight * ((703.0) / (height * height))
BMI = calculateBMI()

print ("""твой индекц это""", str(BMI))

if BMI < 18.5:
	print("Ниже нормального веса")
elif BMI >= 18.5 < 25:
	print("Нормальный вес")
elif BMI >= 25 < 30:
	print("Избыточный вес")
elif BMI >= 30 < 35:
	print("Ожирение I степени")
elif BMI >= 35 < 40:
	print("Ожирение II степени")
elif BMI >= 40:
	print("Ожирение III степени")