"""
exercise2 : 打扑克牌易

Verson : 0.1
Author : 郑超轩
Date   : 2020/02/15
"""
import random
class One_card(object):
    """一张牌"""
    __slots__ = ('_color','_number')
    def __init__(self,color,number):
        """
        :color 花色
        :number 牌面大小
        """
        self._color = color
        self._number = number
    
    @property
    def color(self):
        return self._color
    @property
    def number(self):
        return self._number
    
    def __str__(self):
        """显示---输出为字符"""
        if self._number == 1:
            number_str = 'A'
        elif self._number ==11:
            number_str ='J'
        elif self._number ==12:
            number_str ='Q'
        elif self._number ==13:
            number_str ='K'
        else:
            number_str = str(self._number)
        
        return "%s%s " % (self._color,number_str)
        
    def __repr__(self):
        return self.__str__()

class  All_card(object):
    """一副牌"""
    def __init__(self):
        """
        : _card 总的牌
        : _current_cord 目前发的牌
        """
        self._card =[One_card(color,number) for color in "♣♦♥♠" for number in range(1,14)] 
        self._current_cord = 0 
    
    @property
    def card(self):
        return self._card
    
    def shuffle(self):
        """洗牌"""
        self._current_cord = 0 #洗牌就要保证发的牌为0
        random.shuffle(self._card)
    
    def send_card(self):
        """发牌"""
        card  = self._card[self._current_cord]
        self._current_cord += 1
        return card
    
    def is_not_card(self):
        """判断还有没有牌要发"""
        if self._current_cord == len(self._card):
            return False
        else:
            return True
    
class Player(object):
    """玩家"""
    def __init__(self,name):
        self._name = name
        self._have_card = []
    
    @property
    def name(self):
        return self._name
    @property
    def have_card(self):
        return self._have_card

    def catch_card(self,cards):
        """抓牌"""
        self._have_card.append(cards)
    
    def arrange_card(self,card_key):
        self._have_card.sort(key = card_key)
    

def get_card(cards):
    return (cards.color,cards.number)

def main():
    all_card = All_card() #获得牌
    all_card.shuffle()    #洗牌
    players = [Player('小明'),Player('小黄'),Player('小李'),Player('小张')] #确定玩家
    for  _ in range(13):
        for player in players:
            player.catch_card(all_card.send_card())

    for player in players:
        print(player.name + ':', end=' ')
        player.arrange_card(get_card)
        print(player.have_card)




if __name__ == '__main__':
    main()