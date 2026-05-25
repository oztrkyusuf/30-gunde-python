sayi=int(input("Sayi Gir: "))
if sayi<10 or sayi==10:
    print("Sayi 10'a esit veya kucuk")
elif sayi>10 and sayi<30:
    print("Sayi 10 ile 30 araliginda")
elif (sayi>30) & (sayi<50):
    print("Sayi 30 ile 50 araliginda")
else:
    print("Sayi 50'den buyuk")