if __name__ == '__main__':
    k = int(input("Введите количество критериев: "))
    A = []
    B = []
    S = 0
    print("Введите данные попарного сравнения критериев: ")
    for i in range(k):
        A.append([])
        for j in range(k):
            z = float(input())
            A[i].append(z)
    for i in range(k):
        z = 0.0
        for j in range(k):
            z += float(A[i][j])
        B.append(z)
        S += float(B[i])
    for i in range(k):
        print(i+1, " весовой коэффициент = ", round(B[i]/S, 2))
