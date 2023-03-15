import time # Zamanı hesaplamak için kullandım
import random #Dizi için kullandı.
import soruDort

dizi = [random.randint(0, 10000000) for i in range(1000)]

def linear_search(arr):
    n = len(arr)   #değeri=1 
    max_element = arr[0]   #değeri=1 
    
    for i in range(1, n):   #n-1 kere çalıştığı için değeri n-1
        if arr[i] > max_element:   #değeri=1
            max_element = arr[i]   #değeri=1
    return max_element   #değeri=1

"""
len(arr) islemi, listenin uzunlugunu almak icin O(1) zaman alir.

max_element degiskenine ilk eleman atama islemi, O(1) zaman alir.

for dongusu, n - 1 kez calisir. Dolayisiyla, for dongusunun karmasikligi T(n) = n'dir.

if blogu, bir karsilastirma islemi icerir ve bu islem O(1) zamanda tamamlanir. Bu nedenle, if blogunun karmasikligi T(n) = 1'dir.

max_element degiskeninin degeri, O(1) zamanda guncellenir.

return ifadesi, O(1) zamanda tamamlanir.

Dolayisiyla, toplam zaman karmasikligi T(n) = n * 1 = n'dir.

Sonuc olarak, bu linear search algoritmasi kullanarak yazilan find_max fonksiyonunun zaman karmasikligi, O(n) veya T(n) = n'dir.

"""




def brute_force_find_max(arr):
    n = len(arr)  # atama oldugu icin islem degeri = 1
    max_element = arr[0]  # atama oldugu icin islem degeri = 1
    for i in range(n): # dongu n kere tekrarlandigi icin islem degeri =  n
        for j in range(i+1, n): #T(n) = (n-1) + (n-2) + ... + 1 = n(n-1)/2
            if arr[j] > max_element: # islem degeri = 1
                max_element = arr[j] # islem degeri = 1    
    return max_element #islem degeri = 1
    # O(n^2) zamana esdegerdir. Bu nedenle, bu algoritma buyuk boyutlu dizilerde verimli bir sekilde calismaz.



def main():
    start_timeL = time.time()
    ls = linear_search(dizi)
    end_timeL = time.time()
    total_timeL = end_timeL - start_timeL
    start_timeB = time.time()
    bf = brute_force_find_max(dizi)
    end_timeB = time.time()
    total_timeB = end_timeB - start_timeB

    print("Linear search sonucu -->{0} , Linear search suresi --> {1}".format(ls, total_timeL))
    print("Brute force sonucu -->{0} , Brute force suresi -->{1}".format(bf, total_timeB))



main()
soruDort.main()