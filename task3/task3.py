from sys import argv
from json import load, dump
from collections import deque

def combineTestsValues(tests, values):
    queue = deque([test for test in tests])
    while len(queue) > 0:
        head = queue.popleft()
        if 'value' in head:
            head['value'] = values[head['id']]
        if 'values' in head:
            queue.extend(head['values'])
    return tests

def readTests(path):
    tests = []
    with open(path, 'rt') as file:
        tests = load(file)['tests']
    return tests

def readValues(path):
    values = {}
    with open(path, 'rt') as file:
        valuesList = load(file)['values']
        for record in valuesList:
            values[record['id']] = record['value']
    return values

def main():
    if len(argv) < 4:
        print(f"{argv[0]}: <values.json> <tests.json> <report.json>")
    pathValues, pathTests, pathReport = argv[1:3+1]

    tests  = readTests(pathTests)
    values = readValues(pathValues)
    
    report = combineTestsValues(tests, values)
    with open(pathReport, 'wt') as file:
        dump(report, file)

if __name__ == '__main__':
    main()
