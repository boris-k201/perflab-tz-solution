from sys import argv

def readEllipseCenter(path: str):
    center, radius = None, None
    with open(path, 'rt') as file:
        center = tuple(map(int, file.readline().strip().split()))
        radius = tuple(map(int, file.readline().strip().split()))
    return center, radius

def readPoints(path: str):
    points = []
    with open(path, 'rt') as file:
        for line in file:
            point = tuple(map(int, line.strip().split()))
            points.append(point)
    return points

def ellipseFormula(x: int, y: int, cx: int, cy: int, rx: int, ry: int):
    return ((x-cx)/rx)**2 + ((y-cy)/ry)**2

def isPointInEllipse(center: Tuple[int, int], radius: Tuple[int, int], point: Tuple[int, int]):
    v = ellipseFormula(*point, *center, *radius)
    if v == 1:
        return 0
    elif v < 1:
        return 1
    return 2

def main():
    if len(argv) < 3:
        print(f"{argv[0]}: <circle.txt> <dot.txt>")
    pathEllipseCenter, pathPoints = argv[1:2+1]

    center, radius = readEllipseCenter(pathEllipseCenter)
    points = readPoints(pathPoints)

    for point in points:
        print(isPointInEllipse(center, radius, point))

if __name__ == '__main__':
    main()
