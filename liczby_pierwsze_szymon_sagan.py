def gen(n):
    pierwsze=[]
    i=2
    while len(pierwsze)<n-1:
        jest=False
        for a in pierwsze:
            if i%a==0:
                jest=True
                break
        if not jest:
            pierwsze.append(i)
        i+=1
    pierwsze.insert(0,1)
    return pierwsze
print(gen(30))
