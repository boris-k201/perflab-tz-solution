from sys import argv

def readNumbers(path):
    numbers = []
    with open(path, 'rt') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

def main():
    if len(argv) < 2:
        print(f"{argv[0]}: <numbers.txt>")
        return
    pathNumbers = argv[1]

    numbers = readNumbers(pathNumbers)
    numbers.sort()

    median = numbers[len(numbers)//2]
    numbers = [abs(number - median) for number in numbers]
    sumNumbers = sum(numbers)

    if sumNumbers > 20:
        print("20 ходов недостаточно для приведения всех элементов массива к одному числу")
    else:
        print(sumNumbers)

if __name__ == '__main__':
    main()
