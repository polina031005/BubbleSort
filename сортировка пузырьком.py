def B_S(A):
    
    Flag, n = True, len(A) - 1 #по сути - потенциальное количество перестановок одного значения
    while Flag: 
        Flag = False #останется таким, как только итерация продёт без перестановок => сорт-ка будеьт завершена
        for i in range(n): 
            if A[i] > A[i + 1]: 
                A[i], A[i + 1] = A[i + 1], A[i] #пузырёк всплывает
                Flag = True 
        n -= 1
