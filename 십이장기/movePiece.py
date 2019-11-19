from getSet import makeMap

def cross(target, location):
    checkList = [[target[0] + 1, target[1]], [target[0], target[1] + 1], [target[0] - 1, target[1]],
                 [target[0], target[1] - 1]]

    if location in checkList:
        return True
    else:
        return False


def diagnol(target, location):
    checkList = [[target[0] + 1, target[1] + 1], [target[0] - 1, target[1] + 1], [target[0] - 1, target[1] - 1],
                 [target[0] + 1, target[1] - 1]]

    if location in checkList:
        return True
    else:
        return False

def halfDiagnol(target, location):
    checkList = [[target[0] + 1, target[1] + 1], [target[0] - 1, target[1] + 1]]

    if location in checkList:
        return True
    else:
        return False

class move:


    def King(target, location,cnt):
        if cross(target, location) or diagnol(target, location):

            if makeMap.gameMap[location[0]][location[1]] != 0 and cnt % 2 == 0:
                makeMap.deck2p.append(makeMap.gameMap[location[0]][location[1]])
            elif makeMap.gameMap[location[0]][location[1]] != 0 and cnt % 2 != 0:
                makeMap.deck1p.append(makeMap.gameMap[location[0]][location[1]])

            makeMap.gameMap[location[0]][location[1]] = makeMap.gameMap[target[0]][target[1]]
            makeMap.gameMap[target[0]][target[1]] = 0

        else:
            print('다시 입력')


    def soldier(target, location, cnt):
        if location[0] == target[0] and location[1] - target[1] == 1:

            if makeMap.gameMap[location[0]][location[1]] != 0 and cnt % 2 == 0:
                makeMap.deck2p.append(makeMap.gameMap[location[0]][location[1]])
            elif makeMap.gameMap[location[0]][location[1]] != 0 and cnt % 2 != 0:
                makeMap.deck1p.append(makeMap.gameMap[location[0]][location[1]])

            if location[1] == 0 and cnt % 2 == 0:
                makeMap.gameMap[location[0]][location[1]] = '侯'
                makeMap.gameMap[target[0]][target[1]] = 0

            elif location[1] == 3 and cnt % 2 != 0:
                makeMap.gameMap[location[0]][location[1]] = '侯'
                makeMap.gameMap[target[0]][target[1]] = 0

            else:
                makeMap.gameMap[location[0]][location[1]] = makeMap.gameMap[target[0]][target[1]]
                makeMap.gameMap[target[0]][target[1]] = 0

        else:
            print('다시 입력')

    def firstGeneral(target, location,cnt):

        if cross(target,location):

            if makeMap.gameMap[location[0]][location[1]] != 0 and cnt % 2 == 0:
                makeMap.deck2p.append(makeMap.gameMap[location[0]][location[1]])
            elif makeMap.gameMap[location[0]][location[1]] != 0 and cnt % 2 != 0:
                makeMap.deck1p.append(makeMap.gameMap[location[0]][location[1]])

            makeMap.gameMap[location[0]][location[1]] = makeMap.gameMap[target[0]][target[1]]
            makeMap.gameMap[target[0]][target[1]] = 0
        else:
            print('다시입력')

    def secGeneral(target, location,cnt):

        if diagnol(target,location):

            if makeMap.gameMap[location[0]][location[1]] != 0 and cnt % 2 == 0:
                makeMap.deck2p.append(makeMap.gameMap[location[0]][location[1]])
            elif makeMap.gameMap[location[0]][location[1]] != 0 and cnt % 2 != 0:
                makeMap.deck1p.append(makeMap.gameMap[location[0]][location[1]])

            makeMap.gameMap[location[0]][location[1]] = makeMap.gameMap[target[0]][target[1]]
            makeMap.gameMap[target[0]][target[1]] = 0

        else:
            print('다시 입력')

    def thrGeneral(target, location, cnt):

        if cross(target,location) or halfDiagnol(target,location) :

            if makeMap.gameMap[location[0]][location[1]] != 0 and cnt % 2 == 0:
                makeMap.deck2p.append(makeMap.gameMap[location[0]][location[1]])
            elif makeMap.gameMap[location[0]][location[1]] != 0 and cnt % 2 != 0:
                makeMap.deck1p.append(makeMap.gameMap[location[0]][location[1]])

            makeMap.gameMap[location[0]][location[1]] = makeMap.gameMap[target[0]][target[1]]
            makeMap.gameMap[target[0]][target[1]] = 0

        else:
            print('다시 입력')