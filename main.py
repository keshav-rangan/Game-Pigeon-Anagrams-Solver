def RemoveFromList(thelist, val):
    return [value for value in thelist if value != val]

def FindDic():
    try:
        dicopen = open("DL.txt", "r")
        dicraw = dicopen.read()
        dicopen.close()
        diclist = dicraw.split("\n")
        diclist = RemoveFromList(diclist, '')
        return diclist
    except FileNotFoundError:
        print("No Dictionary!")
        return 
    
def Letterize(word):
    l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    v = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    w = word.lower()
    wl = list(w)
    for i in range(0, len(wl)):
        if wl[i] in l:
            ind = l.index(wl[i])
            v[ind] += 1
    return v

def Convert(letter):
    pv = 0
    f = 0
    for i in range(0, len(letter)):
        wip = (letter[i]*(2**pv))
        f += wip
        pv += 4
    return f
    
def LettersInDic(dic):
    d = {}
    for i in range(0, len(dic)):
        v = Letterize(dic[i])
        Int = Convert(v)
        if Int in d:
            tat = d.get(Int)
            tat.append(dic[i])
            d[Int] = tat
        elif Int not in d:
            d[Int] = [dic[i]]
    return d
        
d = FindDic()
ind = LettersInDic(d)

while True:
    s = input("Enter Letters: ")
    v = Convert(Letterize(s))
    tp = ind.get(v, 'There are no words for these letters.')
    print(tp)

    six = s[:6]
    five = s[:5] + s[5+1:]
    four = s[:4] + s[4+1:]
    three = s[:3] + s[3+1:]
    two = s[:2] + s[2+1:]
    one = s[:1] + s[1+1:]
    zero = s[:0] + s[0+1:]

    splits = [six, five, four, three, two, one, zero]
    
    for i in range(0, len(splits)):
        v2 = Convert(Letterize(splits[i]))
        tp2 = ind.get(v2, '')
        if tp2 != '':
            print(tp2)
        
    if input('Restart? [y/n]') == 'y' or input('Restart? [y/n]') == 'Y':
        pass
    else:
        break

