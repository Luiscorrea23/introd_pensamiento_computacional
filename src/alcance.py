def test1(arg1, arg2, arg3 = 10):
    def otroTest(arg3 = arg3):
        return arg3**2
    testvar = otroTest() + arg1 +arg2

    return test2(testvar, 10)

test3 = 10

def test2(any1, any2):
    return any1 + any2 

testFinal = test1(test3, test2(1,5))
print(testFinal)