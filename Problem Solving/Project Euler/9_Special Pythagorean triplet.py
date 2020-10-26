"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc such that a + b + c = n."""


def specialPythagoreanTriplet(num):
    for a in range(1, int(num / 2)):
        for b in range(a + 1, int(num / 2)):

            c = num - b - a

            if c > b and (c ** 2) == (a ** 2) + (b ** 2):
                return a * b * c


print(specialPythagoreanTriplet(1000))
