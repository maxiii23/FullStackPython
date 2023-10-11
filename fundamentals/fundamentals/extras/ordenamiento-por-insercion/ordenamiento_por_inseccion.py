def ordenar_por_inserción():
    arr = [7,9,6,4,1,3,8,2,5]
    for x in range(len(arr)-1):
        while arr[x+1] < arr[x]:
            arr[x+1], arr[x] = arr[x], arr[x+1]
            if x != 0:
                x = x-1
    print(arr)


ordenar_por_inserción()