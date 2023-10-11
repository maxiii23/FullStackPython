def ordenar_por_seleccion():
    arr = [7,6,9,4,1,3,8,2,5]
    minValue = arr[0]
    for i in range(len(arr)-1):   
        for j in range(i,len(arr)):
            if arr[j] < minValue:
                minValue = arr[j]
                count = j
        arr.pop(count)
        arr.insert(i, minValue)
        minValue = arr[i+1]
    print(arr)
ordenar_por_seleccion()