import random
devam = 'e'
while devam.lower()== 'e':
    sayi=random.randint(1,6)
    tahmin=int(input("Tahmin et...:"))
    skor=5
    while sayi!=tahmin:
            if sayi == tahmin :
                print("kazandınız...: skorunuz...:",skor)
                break
            else:
                print("olmadı...: skorunuz...:",skor)
                skor-=1
                tahmin=int(input("Tahmin et...:"))
            if skor==0 :
                print("kaybettiniz..:  skornuz..:",skor)
                break   
    devam = input ("devam etmek istiyormusunuz(e/h)...:")
    if devam == 'h':
        print("hoşcakalın")
        

    
    
         
    
      
        
        



