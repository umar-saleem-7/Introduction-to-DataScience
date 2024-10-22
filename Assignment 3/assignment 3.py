import functools
import logging

orders = [ 
{"customer": "Alice", "total": 250.5}, 
{"customer": "Bob", "total": "invalid_data"}, 
{"customer": "Charlie", "total": 450}, 
{"customer": "Daisy", "total": 100.0}, 
{"customer": "Eve", "total": -30},
]
def filterValidOrders(orders):
    try:
        validData = filter(lambda orders: (isinstance(orders['total'], (int, float)) and orders['total'] >= 0), orders)
        validData = list(validData)
        return validData
    except Exception as e:
        print("Error:",e)
        return []

filterdata = filterValidOrders(orders)
for order in filterdata:
    print(order)
print('----------------------------------')

def applyDiscount(orders):
    discount = map(lambda order: {'customer': order['customer'], 'total': (order['total'] - order['total'] * 0.1)} if order['total'] > 300 else order, orders)

    discountedOrders = list(discount)
    return discountedOrders

discountedOrders = applyDiscount(filterdata)
for order in discountedOrders:
    print(order)
print('----------------------------------')


def totalSales(orders):
    totalsales = functools.reduce(lambda sum, order: sum + order['total'], orders, 0)
    return totalsales

sales = totalSales(discountedOrders)
print(sales)
print('----------------------------------')



# task 2

class SquareIterator:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        for i in range(1, self.n+1):
            yield i * i


squares = SquareIterator(10)
for square in squares:
    print(square)

print('---------------------------')

def fibonacci_generator(n):
    a, b = 0, 1
    if n == 0:
        yield a
    else:
        yield a
        yield b
    while (a+b) <= n:
        yield a+b
        a, b = b, a+b

fibo = fibonacci_generator(1000)
for fib in fibo:
    print(fib)
print('----------------------------')

# task 3

def divideNumbers(nums, divisor):
    for num in nums:
        try:
            if divisor == 0:
                raise ZeroDivisionError('Division by zero is not allowed!')
            ans = num / divisor
        except ZeroDivisionError as e:
            print(f'Error occurred! while dividing the number \'{num}\' by \'{divisor}\': {e}')
            ans = None
            break
        except ValueError as e:
            print(f'Error occurred! while dividing the number \'{num}\' by \'{divisor}\': {e}')
            ans = None
        except TypeError as e:
            print(f'Error occurred! while dividing the number \'{num}\' by \'{divisor}\': {e}')
            ans = None
        finally:
            if ans:
                print(f'The result of division {num}/{divisor} is: {ans}')
            print('Operation Ended')

nums = [10, 2, 'Three', 5, 7]
divisor = 0
divideNumbers(nums, divisor)
print('-------------------------')


logging.basicConfig(level=logging.ERROR, format='%(message)s')

def exception_decorator(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as e:
            logging.error(f"Exception occurred in function '{function.__name__}':")
            logging.error(f"Exception type: {type(e).__name__}")
            logging.error(f"Exception message: {e}")
            raise
    return wrapper

@exception_decorator
def divide(a, b):
    return a / b

try:
    divide(7, 'a') 
except Exception as e:
    print('Exception handled')


