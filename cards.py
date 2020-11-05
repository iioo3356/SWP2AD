import random

class Card():
    def __init__(self):
        self.cardList = ["sangcheol1.jpg", "sangcheol2.jpg", "sangcheol3.jpg", "sangcheol4.jpg", "sangcheol5.jpg",
                 "penguin1.jpg", "penguin2.jpg", "penguin3.jpg", "penguin4.jpg", "penguin5.jpg", "py1.jpg", "py2.jpg",
                 "py3.jpg", "py4.jpg", "py5.jpg", "xy1.jpg", "xy2.jpg", "xy3.jpg", "xy4.jpg", "xy5.jpg"]

        self.cardDic = {"sangcheol1.jpg": "a1", "sangcheol2.jpg": "a2", "sangcheol3.jpg": "a3", "sangcheol4.jpg": "a4",
                "sangcheol5.jpg": "a5", "penguin1.jpg": "b1", "penguin2.jpg": "b2", "penguin3.jpg": "b3",
                "penguin4.jpg": "b4", "penguin5.jpg": "b5", "py1.jpg": "c1", "py2.jpg": "c2", "py3.jpg": "c3",
                "py4.jpg": "c4", "py5.jpg": "c5", "xy1.jpg": "d1", "xy2.jpg": "d2", "xy3.jpg": "d3", "xy4.jpg": "d4",
                "xy5.jpg": "d5"}

    def randomPicture(self):
        self.card = self.cardList[random.randint(0, 19)]
        return self.card

    def sumPicture(self,c1,c2):
        card1 = self.cardDic[c1]
        card2 = self.cardDic[c2]

        if card1[0] == card2[0]:
            return int(card1[1])+int(card2[1])
        else:
            return 0


    def numPicture(self,c1):
        card1 = self.cardDic[c1]
        return int(card1[1])