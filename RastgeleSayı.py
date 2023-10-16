import random
print(random.randint(2,7))
print(random.random())
print(random.randrange(1,15,2))
print(random.uniform(10,11))
print(random.choice(['2','5','7','8','4','6','1']))
liste=["hakan","can","ali","osman","kılıç","sevgi","ayşe","sinan","zeki","orkun"]
print(random.choice(liste))
random.shuffle(liste)
print(liste)
print(random.sample(liste,3))