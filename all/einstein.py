

# получить массу в интах (кило)
# перевести в джоули по формуле int

def squared(n):
    return n*n


mass = int(input("Input mass(kg): "))
energy = int(300000000)
number_of_joules = squared(energy)*mass
print(number_of_joules)

