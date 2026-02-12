# python mymathlib.py



class NonIntegerException(Exception):
    
    pass



class NegativeIntegerException(Exception):
    
    pass



def power(base, exp):

    return base ** exp



def factorial(n):

    if(isinstance(n, int)):

        if n == 0:

            return 1
        
        elif n == 1:

            return 1
        
        elif n >= 0:

            return n * factorial(n - 1)
        
        else:

            raise NegativeIntegerException(str(n) + ' is a negative integer')            

    else:

        raise NonIntegerException(str(n) + ' is not an integer')



def fibonacci(n):

    if(isinstance(n, int)):

        if n == 0:

            return 0
        
        elif n == 1:

            return 1
        
        elif n >= 0:

            return fibonacci(n - 1) + fibonacci(n - 2)
        
        else:

            raise NegativeIntegerException(str(n) + ' is a negative integer')            

    else:

        raise NonIntegerException(str(n) + ' is not an integer')



def init():

    print('mymathlib.init()')



if __name__ == '__main__':

    init()
