import n_class
adatok = []

def f1(label):
    print(label)
    inputFile("nevezetesegek.txt")

inputFile(file):
    f = open(file, "r")
    for sor in f:
        sor = sor[0:-1].split(";")
        példány =n_class.Nevek(sor[0],sor[1],sor[2])
        adatok.append(példány)
    f.close()
