class MathDojo:
    def __init__(self):
        self.result = 0
        
    def add(self, num, *nums):
        self.result += num
        for n in nums:
            self.result += n
        return self
        
    def subtract(self, num, *nums):
        self.result -= num
        for n in nums:
            self.result -= n
        return self
           
# crear una instancia:
ma = MathDojo()
# para probar:
x = ma.add(2).add(2,5,1).subtract(3,2).result
print(x)	# debería imprimir 5

e = ma.add(5).add(7,1,1).add(4,5,).result
print(e)

m = ma.subtract(4).subtract(40,1,1).subtract(4,5,).result
print(m)