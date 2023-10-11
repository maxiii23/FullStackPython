class Underscore:
    def map(self, iterable, callback):
        for x in range(len(iterable)):
            iterable[x] = callback(iterable[x])
        print(iterable)
        return iterable
    def find(self, iterable, callback):
        for x in iterable:
            if callback(x) == True:
                print(x)
                return x
    def filter(self, iterable, callback):
        for x in iterable:
            if callback(x) == False:
                iterable.remove(x)
        print(iterable)
        return iterable
    def reject(self, iterable, callback):
        for x in iterable:
            if callback(x) == False:
                iterable.remove(x)
        print(iterable)
        return iterable

_ = Underscore()
_.map([1,2,3], lambda x: x*2) # debería devolver [2,4,6]
_.find([1,2,3,4,5,6], lambda x: x>4) # debería devolver el primer valor que sea mayor que 4
_.filter([1,2,3,4,5,6], lambda x: x%2==0) # debería devolver [2,4,6]
_.reject([1,2,3,4,5,6], lambda x: x%2==1) # debería devolver [1,3,5]