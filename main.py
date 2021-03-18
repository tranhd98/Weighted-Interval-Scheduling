import csv
from parse import parse
import bisect


def openFile(filename: str, requests: list):
    with open(filename, 'r') as infile:
        reader = csv.reader(infile, delimiter=",")
        header = next(reader)
        for row in reader:
            start = int(row[0])
            finish = int(row[1])
            value = int(row[2])
            requests.append((start, finish, value))
    return requests


def computeOPT(j: int):
    if j == -1:
        return 0
    elif j >= 0 and M[j] != None:
        return M[j]
    else:
        M[j] = max(requests[j][2] + computeOPT(p[j]), computeOPT(j - 1))
    return M[j]


def findSolution(j):
    if j == -1:
        return
    elif (requests[j][2] + M[p[j]]) >= M[j-1]:
        print(requests[j])
        findSolution(p[j])
    else:
        findSolution(j-1)


if __name__ == '__main__':
    requests = []

    argument = parse()
    openFile(argument.filename[0], requests)
    requests.sort(key=lambda x: x[1])
    p = [0 for x in range(len(requests))]
    startArray = [request[0] for request in requests]
    finishArray = [request[1] for request in requests]
    for index in range(len(startArray)):
        p[index] = (bisect.bisect(finishArray, startArray[index]) - 1)
    M = [0 for x in range(len(requests))]
    for index in range(0, len(M)):
        M[index] = None
    for index in range(len(requests)):
        computeOPT(index)
    findSolution(len(requests) - 1)
