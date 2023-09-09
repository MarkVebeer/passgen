import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

print("Üdvözlöm a cigány jelszó generátorban, itt random jelszavakat generálhat magának, ctrl + c kombinációval léphet ki, viszlát.")

def generate_random_password():
	length = int(input("Add meg a jelszó hosszát: "))

	random.shuffle(characters)

	password = []
	for i in range(length):
		password.append(random.choice(characters))

	random.shuffle(password)

	print("".join(password))

	generate_random_password()


generate_random_password()
