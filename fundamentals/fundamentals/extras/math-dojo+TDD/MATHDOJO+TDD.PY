import unittest

def reverselist(arr):
    arr = arr[::-1]
    return arr
class reverselistTests(unittest.TestCase):
    def testArr1(self):
        self.assertEqual(reverselist([1,2,3]),[3,2,1])
    def testArr2(self):
        self.assertEqual(reverselist([4,6,1,4,6,18,-1,75]), [75,-1,18,6,4,1,6,4])
    def testArr3(self):
        self.assertEqual(reverselist([1,2,3,4,5,6,7,8]), [8,7,6,5,4,3,2,1])
    def setUp(self):
        print("running setUp")
    def tearDown(self):
        print("running tearDown tasks")

def isPalindrome(string):
    invertedStr = string[::-1]
    if string == invertedStr:
        return True
    else:
        return False
class isPalindromeTests(unittest.TestCase):
    def testStr1(self):
        self.assertEqual(isPalindrome('racecar'), True)
    def testStr2(self):
        self.assertEqual(isPalindrome('abc'), False)
    def testStr3(self):
        self.assertEqual(isPalindrome("zzzzzzzzzzzzznzzzzzzzzzzzzz"), True)
    def testStr4(self):
        self.assertEqual(isPalindrome("9999999999989999999999"), False)
    def testStr5(self):
        self.assertEqual(isPalindrome("string"), False)
    def testStr6(self):
        self.assertEqual(isPalindrome("aaabcaaa"), False)
    def setUp(self):
        print("running setUp")
    def tearDown(self):
        print("running tearDown tasks")
def monedas(number):
    arr = [0,0,0,0]
    while number != 0:
        if number - 25 >= 0:
            arr[0] +=1
            number -= 25
        elif number - 10 >= 0:
            arr[1] +=1
            number -= 10
        elif number - 5 >= 0:
            arr[2] +=1
            number -= 5
        elif number - 1 >= 0:
            arr[3] +=1
            number -= 1
    return arr
class monedasTests(unittest.TestCase):
    def testMonedas1(self):
        self.assertEqual(monedas(75), [3,0,0,0])
    def testMonedas2(self):
        self.assertEqual(monedas(99), [3,2,0,4])
    def testMonedas3(self):
        self.assertEqual(monedas(8), [0,0,1,3])
    def testMonedas4(self):
        self.assertEqual(monedas(10), [0,1,0,0])
    def testMonedas5(self):
        self.assertEqual(monedas(41), [1,1,1,1])
    def testMonedas6(self):
        self.assertEqual(monedas(2), [0,0,0,2])
    def setUp(self):
        print("running setUp")
    def tearDown(self):
        print("running tearDown tasks")
def factorial(number):
    fact = 1
    for i in range(1,number +1):
        fact *= i
    return fact
class factorialTests(unittest.TestCase):
    def testFactorial1(self):
        self.assertEqual(factorial(1), 1)
    def testFactorial2(self):
        self.assertEqual(factorial(2), 2)
    def testFactorial3(self):
        self.assertEqual(factorial(3), 6)
    def testFactorial4(self):
        self.assertEqual(factorial(4), 24)
    def testFactorial5(self):
        self.assertEqual(factorial(5), 120)
    def testFactorial6(self):
        self.assertEqual(factorial(6), 720)
    def setUp(self):
        print("running setUp")
    def tearDown(self):
        print("running tearDown tasks")
def fibonacci(number):
    firstN = 0
    secondN = 1
    for i in range(number):
        firstN += secondN
        secondN = firstN - secondN
    return firstN
class fibonacciTests(unittest.TestCase):
    def testFibonacci1(self):
        self.assertEqual(fibonacci(4), 3)
    def testFibonacci2(self):
        self.assertEqual(fibonacci(5), 5)
    def testFibonacci3(self):
        self.assertEqual(fibonacci(6), 8)
    def testFibonacci4(self):
        self.assertEqual(fibonacci(0), 0)
    def setUp(self):
        print("running setUp")
    def tearDown(self):
        print("running tearDown tasks")
if __name__ == '__main__':
    unittest.main()