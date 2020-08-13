n1 = float(input("Digite um número:"))
d = n1 * 2
t = n1 * 3
r = n1 ** (1/2) #ou pow(n1, 2)

print("O dobro de {} é {} \nO triplo de {} é {} \nA raíz quadrada de {} é {:.2f}.".format(n1, d, n1, t, n1, r))
