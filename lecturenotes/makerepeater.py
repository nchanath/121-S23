def makeRepeater(some_text):
    def repeater(number):
        i = 0
        while i < number:
            print(some_text)
            i = i+1
    return repeater
