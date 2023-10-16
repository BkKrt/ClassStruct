import random
print("10 soruluk bir çarpım tablosu testi")
skor=0
yanlış=0
for a in range(10):
    i=random.randint(1,10)
    x=random.randint(1,10)
    soru="{}*{} = ".format(i,x)
    dCvp = i*x #doğru cevap
    cvp=input(soru)
    if int (cvp) == dCvp:
        skor+=1
    else:
        yanlış+=1
print("doğru sayısı:",skor)
print("yanlış sayısı",yanlış)
if skor > 8:
    print("pekiyi")
elif skor > 6:
    print("iyi")
elif skor > 4:
    print(" orta")
else:
    print("Daha çok çalış")