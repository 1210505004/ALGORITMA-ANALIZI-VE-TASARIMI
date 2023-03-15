import random
import time

dizi = [random.randint(0, 10000000) for i in range(1000)]



def quick_sort(arr):
    if len(arr) <= 1: #degeri = 1
        return arr #degeri = 1
    else: #degeri = 1
        pivot = arr[0] #degeri = 1
        left = [] #degeri = 1
        right = [] #idegeri = 1
        for i in range(1, len(arr)): #n kere döneceği için n
            if arr[i] < pivot: #islem degeri = 1
                left.append(arr[i]) # degeri = 1
            else: #degeri = 1
                right.append(arr[i]) #degeri = 1
        return quick_sort(left) + [pivot] + quick_sort(right) # O(log n)

#Quick Sort'un ortalama zaman karmasikligi O(n*log n)'dir


def brute_force_sort(arr):
    for i in range(len(arr)): #n kere döngüye girdiği için n
        for j in range(i+1, len(arr)): #T(n)
            if arr[j] < arr[i]: # islem degeri = 1
                arr[i], arr[j] = arr[j], arr[i] #degeri = 1
    return arr # islem degeri = 1
# O(n^2) zamana esdegerdir.Bundan dolayı çok elemanı olan dizilerde verimli olmayacaktır.


def main():

    quick_sort_time_start = time.time()
    quick_sort(dizi)
    quick_sort_time_end = time.time()
    total_time_quick_sort = quick_sort_time_end - quick_sort_time_start
    print("\n")
    print("Quick sort suressi -->", total_time_quick_sort)


    brute_force_sort_start = time.time()
    brute_force_sort(dizi)
    brute_force_sort_end = time.time()
    total_time_brute_force_sort = brute_force_sort_end - brute_force_sort_start
    print("Brute force sort suresi -->", total_time_brute_force_sort)

"""
Quick sort algoritmasinin n elemanli bir dizinin siralanmasi icin harcanan zamanin matematiksel ifadesi T(n)'dir..
Bu ifade, pivot elemaninin secimine, dizinin boyutuna ve dizi elemanlarinin ozelliklerine baglidir.

Siralanacak verilerin boyutuna gore Quick sort algoritmasinin O(n) tablosu degisebilir.
Ancak, genel olarak Quick sort, O(n log n) karmasikligina sahiptir.
Bu karmasiklik, dizinin boyutuna gore logaritmik artis gosterir ve n elemanli bir dizi icin O(n log n) zaman alir.

Ornegin, bir dizinin boyutu 1000 olsun.
Quick sort, bu diziyi siralamak icin O(1000 log 1000) = O(1000 x 3) = O(3000) zaman alir.
Bu, büyük veri setleri icin oldukca hizli bir siralama algoritmasidir.

"""