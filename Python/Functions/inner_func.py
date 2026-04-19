def outer():
    print("In outer function")

    def inner():
        print("In inner function")

    # inner() # Calling the inner function
    return inner

something =outer()
something()