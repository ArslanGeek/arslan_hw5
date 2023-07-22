A = [i for i in range(1, 101)]
print(A)

def binary_search(A, Val):
    pos = None
    N = len(A)
    ResultOk = False
    First = 0
    Last = N - 1

    while True:
        if First < Last:
            Middle = (First+Last) // 2
            if Val == A[Middle]:
                First = Middle
                Last = First
                ResultOk = True
                pos = Middle
            else:
                if Val > A[Middle]:
                    First = Middle + 1
                else:
                    Last = Middle - 1
        else:
            if ResultOk == True:
                print(f'Element is found on position {pos}')
                break
            else:
                print('Element is not found')
                break

binary_search(A, 23)
binary_search(A, 12)
binary_search(A, 91)