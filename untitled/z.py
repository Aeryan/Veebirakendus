global sum
sum = 0

def kiirsort(jarj):
    global sum
    sum += 1
    if len(jarj) <= 1:
        return jarj
    vordne = [jarj[0]] # loo uus järjend, kus on järjendi jarj esimene element
    vaiksem = []
    suurem = []
    for elem in jarj[1:]:
        if elem < vordne[0]:
            vaiksem.append(elem)
        elif elem == vordne[0]:
            vordne.append(elem)
        else:
            suurem.append(elem)
    return kiirsort(vaiksem) + vordne + kiirsort(suurem)

a = []
for i in range(36):
    a.append(36-i)
kiirsort(a)
print(sum)