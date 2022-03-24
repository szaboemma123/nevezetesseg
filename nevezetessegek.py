import n_class
adatok = []

def f1(label):
    print(label)
    inputFile("nevezetesegek.txt")
    print("\tFranciaország")
    print("\tUSA")
    print("\tKína")
    print("\tMagyarország")
    print("\tIndia")
    print("\tAusztrália")

def f2(label):
    print(label)
    orszagnev = input("\tKérek egy országot: ")
    for i in range(len(adatok)):
        nev = adatok[i][0]
        if(orszagnev == adatok):
            print(adatok[i][0], adatok[i][1], adatok[i][2],)
            
      
    
def inputFile(file): 
    f = open(file, "r")
    for sor in f:
        sor = sor[0:-1].split(";")
        példány =n_class.Nevek(sor[0],sor[1],sor[2])
        adatok.append(példány)
    f.close()


f1("1.feladat")
f2("2.feladat")
