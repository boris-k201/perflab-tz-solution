from sys import argv

def circularArrayTraverse(n: int, m: int):
    result = [1]
    i = m
    while i != 1:
        result.append(i)
        i = (i + m - 2) % n + 1
    return result

def main():
    if len(argv) < 5:
        print(f"{argv[0]}: <n1> <m1> <n2> <m2>")
    n1, m1, n2, m2 = list(map(int, argv[1:4+1]))
    solution1 = circularArrayTraverse(n1, m1)
    solution2 = circularArrayTraverse(n2, m2)
    print(*solution1, *solution2, sep='')

if __name__ == '__main__':
    main()
