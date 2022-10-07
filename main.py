# Write a program with numbers that range from 0 to 100
# For multiples of 3, print 'Fizz' in place of the number
# For multiples of 5, print 'Buzz' in place of the number
# For multiples of both 3 and 5, print 'FizzBuzz' in place of the number

for x in range(1, 101):  # this will print 1 to 100. If I set 100 as a parameter, it would stop at 99

    #  this conditional statement is placed first. I placed it last when I first tried it.
    # But the program failed to execute properly due to the other conditions executing first.
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    if x % 3 == 0:  # the modulo operator returns the remainder of division 3/3 would equal to 0 - multiple of 3
        print("Fizz")  # this will print in place of the number that is a multiple of 3
    elif x % 5 == 0:
        print("Buzz")
