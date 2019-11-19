from getSet import makeMap

class select:

    def putPiece(self,target,location,cnt):

        if cnt % 2 != 0:
            makeMap.gameMap[location[0]][location[1]] = makeMap.deck2p[target]

        else:
            makeMap.gameMap[location[0]][location[1]] = makeMap.deck1p[target]