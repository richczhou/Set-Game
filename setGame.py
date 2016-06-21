# Written by Richard Zhou
# Plays the card game Set! better than Sandra ever could.

import random  # needed for shuffle


class SetGame:
    """Based on the Set! card game and written purely
    to try to make Sandra never play the game again.
    And maybe because Python is fun. Maybe."""

    # All the card attributes
    cardNums = ["one ", "two ", "three "]
    cardShading = ["open ", "striped ", "solid "]
    cardColor = ["red ", "green ", "blue "]  # note blue may be purple
    cardShapes = ["diamond", "squiggle", "oval"]

    def __init__(self):  # the class constructor
        self.deck = []  # here we create a set deck by going through 3^4 4-digit integer "cards"
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    for l in range(1, 4):
                        self.deck.append(1000 * i + 100 * j + 10 * k + 1 * l)  # every card in deck is a 4digit
                                                                # num w/ a digit representing a trait
        random.shuffle(self.deck)  # shuffle newly created deck

    def __str__(self):  # debug only pls ignore just making sure all 81 cards are present
        print(self.deck)
        print(len(self.deck))  # 81 cards, working

    def shuffleDeck(self):  # here just for playing around in shell
        """Shuffles the deck pseudo-randomly."""
        random.shuffle(self.deck)

    def showDeck(self):  # debug only pls ignore
        """Outputs the deck as a list of 4-digit integers."""
        print(self.deck)

    # #########|GAME DEVELOPMENT FROM HERE ON|##########

    def showCard(self, cardInt):
        """Given a 4-digit integer \"card\", it will output the str version of it."""
        # Getting each digit of the 4-digit card
        thouDigit = int(cardInt / 1000)
        hunsDigit = int((cardInt % 1000) / 100)
        tensDigit = int((cardInt % 100) / 10)
        unitDigit = int(cardInt % 10)

        # matches each digit to a trait
        print(str(self.cardNums[thouDigit - 1]) + str(self.cardShading[hunsDigit - 1]) +
              str(self.cardColor[tensDigit - 1]) + str(self.cardShapes[unitDigit - 1]), end='')  # end="" means no newline
        if thouDigit > 1:  # here is just to add an 's' if plural so grammar game on point
            print('s')
        else:
            print('')  # print empty string for newline

    def setCard(self, card1, card2):
        """Given two 4-digit integer \"cards\", it will return the exact
        4-digit integer \"card\" needed to create a Set!."""
        # getting the digits of each 4-digit card
        thouDigit1 = int(card1 / 1000)
        hunsDigit1 = int((card1 % 1000) / 100)
        tensDigit1 = int((card1 % 100) / 10)
        unitDigit1 = int(card1 % 10)
        ###########################
        thouDigit2 = int(card2 / 1000)
        hunsDigit2 = int((card2 % 1000) / 100)
        tensDigit2 = int((card2 % 100) / 10)
        unitDigit2 = int(card2 % 10)

        self.flags = [0, 0, 0]  # flag array
        # setting thousands digit
        if thouDigit1 == thouDigit2:      # if the traits are the same then we
            thouDigit3 = thouDigit1 - 1    # make sure the trait we want is too
        else:
            self.flags[thouDigit1 - 1] = 1  # otherwise pick the "other one"
            self.flags[thouDigit2 - 1] = 1
            thouDigit3 = self.flags.index(0)  # the index() just finds first index with '0'
        # setting hundreds digit
        self.flags = [0, 0, 0]            # reset the flag array and do the same stuff again for each digit
        if hunsDigit1 == hunsDigit2:
            hunsDigit3 = hunsDigit1 - 1
        else:
            self.flags[hunsDigit1 - 1] = 1
            self.flags[hunsDigit2 - 1] = 1
            hunsDigit3 = self.flags.index(0)
        # setting tens digit
        self.flags = [0, 0, 0]
        if tensDigit1 == tensDigit2:
            tensDigit3 = tensDigit1 - 1
        else:
            self.flags[tensDigit1 - 1] = 1
            self.flags[tensDigit2 - 1] = 1
            tensDigit3 = self.flags.index(0)
        # setting units digit
        self.flags = [0, 0, 0]
        if unitDigit1 == unitDigit2:
            unitDigit3 = unitDigit1 - 1
        else:
            self.flags[unitDigit1 - 1] = 1
            self.flags[unitDigit2 - 1] = 1
            unitDigit3 = self.flags.index(0)

        # return the card we need
        return(1000 * (thouDigit3 + 1) + 100 * (hunsDigit3 + 1) + 10 * (tensDigit3 + 1) + (unitDigit3 + 1))

    def drawTriple(self):
        """\"Draws\" three cards by popping from gameDeck to table."""
        for t in range(0, 3):    # for the first 3 elements
            if(len(self.gameDeck) > 0):   # as long as there are cards in the deck
                self.table.append(self.gameDeck.pop())  # remove from deck and put them to table

    def getSet(self, index1, index2, index3):  # assuming index1-3 are sorted
        """Calls Set! and removes it from the table, returning a Set!."""
        self.oneSet = []
        self.oneSet.append(self.table.pop(index3))  # removes the cards from the table and adds to Set!
        self.oneSet.append(self.table.pop(index2))  # Notice the backwards order as to not disturb
        self.oneSet.append(self.table.pop(index1))  # the indices before it
        return self.oneSet

    def isSet(self):   # not sure if need deck param
        """Checks if there is a Set! on the table and if so, takes it."""
        for j in range(0, len(self.table) - 1):  # next two loops pretty much get 2 distinct cards
            for k in range(j + 1, len(self.table) - 1):  # we always start from (last card)+1 so diff cards
                # find the corresponding set with the 2 cards (j and k)
                jesus = self.setCard(self.table[j], self.table[k])  # jesus b/c we hope it exists
                for l in range(k + 1, len(self.table) - 1):  # look at rest of the table
                    if self.table[l] == jesus:  # if we find a Set!
                        self.sets.append(list(self.getSet(j, k, l)))  # redundancy on list() I think but good to have
                        if len(self.table) < 12:  # if the table size goes under 12 then draw
                            self.drawTriple()
                        return  # every time we find a set we return to kill the function

    def listSets(self):
        """Displays all Set!'s obtained."""
        print("=================|SETS|====================")
        for singleSet in self.sets:  # for every Set! in our Set!'s found
            self.showCard(singleSet[0])  # we just display the 3 cards
            self.showCard(singleSet[1])
            self.showCard(singleSet[2])
            print("===========================================")

    def showTable(self):
        """Prints out the current cards in play."""
        print("++++++++++++++TABLE+++++++++++++++++++")
        for aCard in self.table:   # string-ify's all cards on table
            self.showCard(aCard)
        print("++++++++++++++++++++++++++++++++++++++")
        print("")   # always to space out stuff with casual newline

    def playSet(self):
        """Plays a solo game of Set! with the computer. RIP Sandra."""
        self.gameDeck = list(self.deck)  # makes a copy of the Set! deck
        random.shuffle(self.gameDeck)  # shuffles the newly created deck
        self.table = []  # the cards (usually 12) on the playing field
        self.sets = []  # will hold the Set's we find (this is a list of lists)
        for i in range(0, 3):  # this puts the starting 9 cards.
            self.drawTriple()   # bc it needs to draw on a deadlocked board
        while len(self.table) != 0 and len(self.sets) < 20:  # we stop @ twenty
            self.drawTriple()            # sets bc 20 card or 7 set deadlock
            self.showTable()
            self.isSet()
        lastLen = len(self.sets)  # this is so we know when to refresh table
        for i in range(0, 10):  # solve "manually" so if it is deadlocked
            self.drawTriple()    # if board is impossible it doesn't get stuck
            if len(self.sets) > lastLen:  # refresh table state if we find Set!
                self.showTable()
                lastLen = len(self.sets)  # and increase it for next iteration
            self.isSet()
        self.listSets()     # shows all the Set!'s we found


# actually running the game here
s = SetGame()
s.playSet()
