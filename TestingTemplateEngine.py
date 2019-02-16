variableDict = {}
def parse(fileName):
    with open(fileName, "r") as file:
        for line in file.readlines():
            print(line)
        # line = file.readline()
        # print(line)

parse("file.ttl")