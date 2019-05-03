# Soal 1: Fungsi pangkat tidak boleh pakai ** atau pow

def pangkat(x, y):
    a = 1
    b = 1
    while (b <= y):
        a = a * x
        b = b + 1
    return a
 
print(pangkat(2, 2))
print(pangkat(3, 3))
print(pangkat(10, 5))
