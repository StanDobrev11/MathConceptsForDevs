def summator(a):
    def inner_summator(b):
        return a + b

    return inner_summator


print(summator(5)(1))