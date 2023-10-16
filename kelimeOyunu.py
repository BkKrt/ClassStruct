import random
Liste = ["pythpn","print","random","while","choice"]
kelime=random.choice(Liste)
adam= ['''
  +----+
  o    l
 /l\   l  
 / \   l
      ---''','''
 +----+
  o    l
 /l\   l  
 /     l
      ---''','''
 +----+
  o    l
 /l\   l  
       l
      ---''','''
 +----+
  o    l
 /l    l  
       l
      ---''','''
 +----+
  o    l
 /     l  
       l
      ---''','''
 +----+
  o    l
       l  
       l
      ---''','''
       l
       l  
       l
      ---''','']

dogruHarf = []
yanlısHARF = []
hak = len(adam)

while hak > 0 :
    out = ""
    for h in kelime :
        if h in dogruHarf:
            out+=h
        else:
            out+="_"
    if out == kelime:
        break
    print("kelime: ",out)    
    print (adam[hak-1])      
    girHarf = input() 
    if girHarf in dogruHarf or girHarf in yanlısHARF:
        print(girHarf,"zaten girildi")
    elif girHarf in kelime:
        print("doğru harf ")
        dogruHarf.append(girHarf)
    else:
        print("yanlış harf")
        hak-=1
        yanlısHARF.append(girHarf)

if hak!=0:
    print("doğru bildiniz")
