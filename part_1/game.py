import random

numper = random.randint(0, 101)
while True:
	answer = input("Введите число: ")
	if not answer or answer == "exit":
		break

	if not answer.isdigit():
		print("Введите правильное чилос!")

	user_answer = int(answer)

	if user_answer > numper:
		print("Загаданное число меньше")
	elif user_answer < numper:
		print("Загаданное число больше")
	else:
		print("Чило угадано")
		break