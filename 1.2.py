import math

def discriminant(a,b,c):

    return b*b-4*a*c


def larger_root(p, q):
    D = float(discriminant(1,p,q))
    if D<0:
        print("нет корней")

    return (-p + math.sqrt(D)) / 2


def smaller_root(p, q):
    D = float(discriminant(1, p, q))
    return (-p - math.sqrt(D)) / 2


def main():
    print("введите p и q для вашего квадратного уравнения")
    p = float(input())
    q = float(input())
    print(discriminant(1, p, q))
    print(smaller_root(p, q))
    print(larger_root(p, q))


main()
