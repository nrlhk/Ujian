# Return function tanpa reverse

def balikPosisi(list):
    balikPosisiList = []
    i = len(list) - 1

    while i >= 0 :
        balikPosisiList.append(list[i]) 
        i -= 1
    return balikPosisiList

print(balikPosisi([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(balikPosisi(['A', 'B', 'C', 'D', 'E', 'F', 'G']))
print(balikPosisi(['Messi', 'Suarez', 'Coutinho', 'Dembele', 'Rakitic']))
