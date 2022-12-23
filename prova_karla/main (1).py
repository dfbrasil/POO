from person import Person
from friend import Friend
from hobby import Hobby
from telemarketing import Telemarketing
from insect import Insect
from nuisance import Nuisance
from mosquito import Mosquito
from butterfly import Butterfly

# ----------------------QUESTÃO 01 -------------

# p1 = Person("Karla", 20)
# print(f"Name: {p1.get_name()}")
# print(f"Age: {p1.get_age()}")

# p1.set_name("Julyana")
# p1.set_age(19)

# print(p1)


# p2 = Person("Joana", 1)
# print(p2)

# p3 = Person("Rafael", 150)
# print(p3)

# p4 = Person("Matheus", 0)
# p5 = Person("Yara", 151)

# # ----------------------QUESTÃO 02 -------------
# h1 = Hobby.music
# print(h1._name_)

# ----------------------QUESTÃO 03 -------------
# f1 = Friend("André", 16, "lol")
# print(f1)
# f1.chill()

# friends = []
# print(f1.play(friends))

# friends = ["Alisson"]
# print(f1.play(friends))

# friends = ["Alisson", "Ana"]
# print(f1.play(friends))

# friends = ["Alisson", "Ana", "Kelvin", "Bia"]
# print(f1.play(friends))

# # ----------------------QUESTÃO 05 -------------
# Nuisance.register(Telemarketing)
# t1 = Telemarketing("Roberta", 19)
# print(t1.give_sales_pitch())
# print(t1.annoy())

# ----------------------QUESTÃO 06 -------------
Nuisance.register(Mosquito)
m1 = Mosquito("Culex tarsalis")
print(m1)
print(m1.annoy())
print(m1.buzz())

# ----------------------QUESTÃO 07 -------------
i = Insect("Wasp")
print(i)

# ----------------------QUESTÃO 08 -------------
colors = []
b1 = Butterfly("Morpho", colors)
print(b1)

colors = ["yellow", "red"]
b2 = Butterfly("Phoebis", colors)
print(b2)


colors = ["yellow", "blue"]
b3 = Butterfly("Morphus", colors, b1)
print(b3)

# # ----------------------QUESTÃO 09 -------------
# f3 = Friend("Carlos", 22, "tocar violão")
# f4 = Friend("Carlos", 22, "tocar violão")
# f5 = Friend("Daniela", 22, "tocar violão")

# # __eq__ foi implementado na classe friend (friend.py)
# if f3.__eq__(f4): 
#     print("Amigos iguais")
# else:
#     print("Amigos diferentes")

# if f3.__eq__(f5): 
#     print("Amigos iguais")
# else:
#     print("Amigos diferentes")
