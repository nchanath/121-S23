def makeGetter(prompt, conversion, condition):
    def getter():
        while True:
            entry = input(prompt)
            value = conversion(entry)
            if condition(value):
                return value
            print("Not what we requested.")
    return getter
