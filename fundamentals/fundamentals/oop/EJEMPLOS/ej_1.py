arr = [8,1,5,3,2,0]

def bubbleSort(arr):
    for i in range(len(arr)):
        print("\n","*"*80, "\nindex", i, "value", arr[i])
        print("comparing", arr [i], arr[i+1])
        if arr[i > arr[i+1]]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            print("awapped", arr[i], arr[i+1])
        else :
            print("no need to swap", arr[i], arr[i+1])


bubbleSort(arr)    



[]