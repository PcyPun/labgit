dataset = {54,12,30,77,64,19}
A=0
B=0
C=0
D=0
F=0
for x in dataset:
    print(x)
    while x != 'x' :
        x = input("x = ")
        if x.isnumeric() :
            if float(x) >= 80 :
                print("A")
                A=A+1
            elif float(x) >= 70 :
                print("B")
                B=B+1
            elif float(x) >= 60 :
                print("C")
                C=C+1
            elif float(x) >= 50 :
                print("D")
                D=D+1
            else:
                print("F")
                F=F+1
        print("A ="+str(A))
        print("B ="+str(B))
        print("C ="+str(C))
        print("D ="+str(D))
        print("F ="+str(F))
    