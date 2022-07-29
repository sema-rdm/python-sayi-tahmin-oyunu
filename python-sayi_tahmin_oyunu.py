#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from random import randint
rand=randint(1, 10)
sayac=0
while True:
    sayac+=1
    sayi=int(input("1 ile 10 arasında bir değer girin (0 cıkış):"))
    if(sayi==0):
        print("oyunu iptal ettiniz")
        break
    elif sayi<rand:
        print("daha yüksek bir sayı giriniz:")
        continue
    elif sayi>rand:
        print("daha küçük bir sayı giriniz:")
        continue
    else:
        print("rastgele seçilen sayı {0}",format(rand))
        print("tahmin sayısı {0}",format(sayac))


# In[ ]:




