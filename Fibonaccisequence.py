def fib(n):
    # Checks if the input is 1 or 0
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        # If the input is not one or zero then use this equation
        return fib(n-1) + fib(n-2)

    