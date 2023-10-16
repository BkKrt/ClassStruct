import random
devam='e'
while devam.lower() =='e':
    Liste = ["taş","kağıt","makas"]
    pc=random.choice(Liste)
    player=input('[Taş-Makas-Kağıt] birini seçiniz..:').lower()

    print('bilgisayar',pc,' seçti')
    print('sen',player,'seçtin')

    if pc==player :
        print("Berabere")
    elif (pc == "kağıt" and player =="taş") or (pc == "taş" and player =="makas") or (pc == "makas" and player =="kağıt"):
        print ("Kaybettin")
    else:
        print("Kazandın..:")
    
    devam= input("devam etmek istiyormusunuz?(e/h)").lower()
    if devam == 'h':
        print("hoşcakalın")
    

