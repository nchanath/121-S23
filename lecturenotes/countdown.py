import time, sys

#
# countdown.py
#
# This program counts down by an amount, ending a 1.
# For example, it might start at 101, count down by 20
# and so it will end with counts of 41, 21, and 1.
#
# It dramatically pauses, putting all the counts on the
# same line, just to make the console output interesting.
#

# Greet the user and ask for count parameters.
print("This program will count down to 1 by an amount.")
start = int(input("Enter a value to start near: "))
decrement = int(input("Enter an amount to step down: "))

# Do the counting once they hit RETURN.
print("Ready? Counting down to 1:")
input("[Hit RETURN]")

# Figure out a good place to start that leads to 1.
count = start - ((start - 1) % decrement)

while count > 1:
    
    #
    # Output the count, then pause.
    print(str(count) + "...", end='') # Keep on the same line.
    sys.stdout.flush()
    time.sleep(1)

    #
    # Go to the next countdown value.
    count = count - decrement
    
# Output the last count (of the value 1).    
print("1!!!!!")
