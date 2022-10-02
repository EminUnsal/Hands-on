def parantez(test):
    #len(test) tek ise gecersiz
    if len(test)%2 == 1:
        return False
    par_dict = {'(':')','{':'}','[':']'}
    liste = []
    for i in test:
        #Acma parantezi ise listenin sonuna ekle
        if i in par_dict.keys():
            liste.append(i)
        #Kapama parantezi ise;
        else:   
            if liste == []: # 1. Durum Liste bos olursa False
                return False
            acma_parantezi = liste.pop() #pop son elemani listeden siler ve döndürür ve  bu bir acma parantezidir
            if i != par_dict[acma_parantezi]: # acma parantezinin value degeri;  (karsiligi olan kapama parantezi) 
                return False # döngüdeki bütün acma parantezleri kapama parantezleri ile eslesirse döngü true deger döndürür
    return liste == []
    #Eger hepsi acma parantezi olsa liste bos olmayacagi icin False döndürür.

print(parantez("()"))
print(parantez("()[]{}"))
print(parantez("(]"))
print(parantez("([)]"))
print(parantez("{[]}"))
print(parantez("((["))

        