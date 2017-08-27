# Function Decorators
[aortiz](http://programmingbits.pythonblogs.com/27_programmingbits/archive/50_function_decorators.html) | 31 January, 2009 09:50

The Python programming language has an interesting syntactic feature called a decorator. Let's use an example in order to explain how and why you would want to use a Python decorator.

NOTE: All Python code examples presented here are based in Python 3.0. Full source code: [function_decorators.py](http://programmingbits.pythonblogs.com/gallery/27/function_decorators.py)

Suppose we want to compute the Fibonacci numbers using a recursive function1. The following function definition does the trick:

```Python
def fib(n):
    if n in (0, 1):
        return n
    else:
        return fib(n - 1) + fib(n - 2)
```

We can now test the function with different input values:

```
>>> fib(0)
0
>>> fib(1)
1
>>> fib(4)
3
>>> fib(10)
55
>>> fib(30)
832040
>>> fib(35)
9227465
```

If you've actually typed these examples in a Python shell, you've probably noticed that obtaining a result takes longer for bigger inputs. In order to make it run faster, we can use a technique called memoization. A memoized function stores in a cache the results corresponding to some set of specific inputs. Later calls, with previously computed inputs, return the results stored in the cache, thus avoiding their recalculation. This means that the primary cost of a call with certain parameters is taken care of during the first call made to the function with those same parameters.

Instead of modifiying the fib function directly, it's better to write a reusable memoizing function:

```Python
def memoize(f):
    cache = {}
    def helper(x):
        if x not in cache:            
            cache[x] = f(x)
        return cache[x]
    return helper
```

The memoize function wraps another function, called helper, which is going to provide additional functionality to the function received through parameter f. The helper function is actually a lexical closure, that is, a function object that remembers the variable bindings that were in its scope when it was created. In this case, helper remembers variables f and cache, which happen to hold a function object and a dictionary, respectively. The last statement in memoize just returns to its caller the helper lexical closure.

Type the following code, and you'll notice right away a speed increase when calling fib. The speedup can be appreciated even in the very first call because the memoization immediately boosts all the recursive calls inside fib's definition.

```
>>> fib = memoize(fib)
>>> fib(50)
12586269025
```

The assignment in the first line can be read as: the fib function is being decorated by the memoize function. Because this is such a common programming idiom in Python, there's a special decorator syntax to simplify its use. This syntax was originally inspired by Java's annotations: just above the definition of the function that is to be decorated, place an at sign (@) followed by the name of the decorator function.

In other words, this Python syntax:

```Python
@some_decorator
def some_function():
    # function body...
```

is equivalent to:

```Python
def some_function():
    # function body...
some_function = some_decorator(some_function)
```

Most should agree that the @ notation is more readable and less error prone.

In order to use the Python decorator with our Fibonacci + memoization example, we would have to rewrite as follows:

```Python
def memoize(f):
    # Same code as before...

@memoize
def fib(n):
    # Same code as before...
```

The memoize function shows the general structure that a typical function decorator should have: it receives a function f as its input parameter, and it returns another function that attaches some additional responsibilities to f.

Another interesting thing about Python decorators is that you can chain two or more together. Let's extend our example in order to incorporate a tracing decorator that will display a message before the decorated function gets called and also when it returns.

```Python
def memoize(f):
    # Same code as before...

def trace(f):
    def helper(x):
        call_str = "{0}({1})".format(f.__name__, x)
        print("Calling {0} ...".format(call_str))
        result = f(x)
        print("... returning from {0} = {1}".format(
              call_str, result))
        return result
    return helper

@memoize
@trace
def fib(n):
    # Same code as before...
```    

Notice the use @memoize and @trace just before the definition of fib. Now, when invoking fib, first the memoize decorator gets called, then the trace decorator, and finally the original fib code. Check this example:

```Python
>>> fib(5)
Calling fib(5) ...
Calling fib(4) ...
Calling fib(3) ...
Calling fib(2) ...
Calling fib(1) ...
... returning from fib(1) = 1
Calling fib(0) ...
... returning from fib(0) = 0
... returning from fib(2) = 1
... returning from fib(3) = 2
... returning from fib(4) = 3
... returning from fib(5) = 5
5
```

Python has three built-in functions that are intended to be used as function decorators:

- classmethod: used to indicate that the decorated method is a class method, similar to those in Smalltalk or Ruby.
- staticmethod: used to indicate that the decorated method is a static method, like those in C++, C# or Java.
- property: used to decorate methods that will be used to get, set and delete object properties.

It's also worth noting that Python 3.0 not only allows you to decorate functions, but also complete classes. Hopefully, I'll take some time to write about these specific kinds of decorators in a a future post.

## Notes

Yes, I know that using recursion to implement the Fibonacci sequence is very inefficient. But that was my intention. I wanted a simple algorithm that produces a perceivable time delay for certain inputs.

## Further Reading
[PEP: 318 Decorators for Functions and Methods](http://www.python.org/dev/peps/pep-0318/)
