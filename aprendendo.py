idade = 20
if idade >= 18:
	print("Você é maior de idade.")
elif idade < 18 and idade > 12:
	print("Você é adolescente.")
else:
	print("Você é criança.")


for i in range(5):
	print(i)


contador = 0
while contador < 5:
	print(contador)
	contador += 1

def saudacao(nome):
	print(f"Olá, {nome}!")

saudacao("João")

