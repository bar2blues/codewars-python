def reverse(n):
    """Returns n with all digits reversed. Assume positive n."""
    #your code here
    r = 0
    while n:
        r = r*10 + n%10
        n //= 10
    return r


# Instructions
#
# Impliment the reverse function, which takes in input n and reverses it. For instance, reverse(123) should return 321.
# You should do this without converting the inputted number into a string.