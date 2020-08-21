"""
exercise1 :奥特曼打小怪兽
描述：
类：
1）奥特曼参数：名字，生命值（绑定），魔法值
2）奥特曼模块：
    1.攻击：普通攻击，必杀技（使用魔法值，打掉对方至少50点或四分之三的血)必杀技失败使用普通攻击，魔法攻击
    2.魔法值，：恢复
    3）显示（返回）：生命值和魔法值
3）怪兽模块:
    1.攻击:普通攻击
    2.显示（返回）：生命值

函数：
1）判断小怪兽是否还活着
2）选中一个活着的小怪兽
3）显示奥特曼或者怪兽的信息
"""
from abc import ABCMeta,abstractmethod
from random import randint,randrange

class Fighter(object,metaclass = ABCMeta):

    __slots__  = ('_name','_hp')

    """抽象函数"""
    def __init__(self,name,hp):
        """
        :name  名字
        :hp    生命值
        """
        self._name = name
        self._hp   = hp
    
    @property
    def name(self):
        return self._name
    @property
    def hp(self):
        return self._hp
    @property
    def alive(self):
        return self._hp > 0

    @hp.setter  
    def hp(self,hp):
        """保证不小于0"""
        self._hp = hp  if hp>=0 else 0
    
    @abstractmethod 
    def attack(self,other):
        """
        攻击
        : other :攻击对象
        """
        pass


class  Ultraman(Fighter):

    __slots__ = ('_name','_hp','_mp')  

    def __init__(self,name,hp,mp):
        """
        :name 名字
        :hp   生命值
        :mp   魔法值
        """
        super().__init__(name,hp)
        self._mp = mp
     
    def attack(self,other):
        """普通攻击（随机伤害1-15）"""
        other.hp -= randint(1, 15)
    
    def unique_attack(self,other):
        """
        必杀技 : 使用魔法值，打掉对方至少50点或四分之三的血)必杀技失败使用普通攻击
        """
        if self._mp>=50:
            self._mp -=50
            injury = self.hp*3//4
            injury = injury if injury>=50 else 50
            self.hp -=injury
            return True
        else:
            self.attack(other)
            return False
    
    def magic_attack(self,others):
        """others:代表全部的小怪物"""
        if self._mp >=30:
            self._mp -= 30
            for other in others:
                if other.alive > 0:
                    other.hp -= randint(1,15)
            return True
        else:
            return False
    
    def magic_recover(self):
        """魔法恢复"""
        recover  = randint(1,10)
        self._mp += recover
        return  recover   #显示魔法恢复的多少
    
    def __str__(self):
        return "%s 的生命值是%d \n  魔法值是%d" % (self.name,self.hp,self._mp)
    

class Griffin(Fighter):
    "怪兽模块"

    def attack(self,other):
        """普通攻击"""
        other.hp -= randint(1,15)
    
    def __str__(self):
        return "%s 的生命值是%d" % (self.name,self.hp)
    

def is_alive(fighters):
    """判断怪兽活着的情况--全部"""
    for fighter in fighters:
        if fighter.alive > 0:
            return True
    return False

def select_griffin(griffins):
    griffin_len = len(griffins)
    while True:
        index = randrange(griffin_len)
        griffin = griffins[index]
        if griffin.alive>0:
            return griffin


def display_show(ultraman,griffins):
    """显示奥特曼和怪兽的情况"""
    print(ultraman)
    for  griffin in griffins:
        print(griffin,end ="  ")


def main():
    u = Ultraman('迪迦',800,120)
    g1 = Griffin('怪物A',120)
    g2 = Griffin('怪物B',150)
    g3 = Griffin('怪物C',180)
    g_all = [g1,g2,g3]

    #表示回合
    fight_around = 1 
    while u.alive and is_alive(g_all):
        print("\n===========第 %2d 回合==========" % (fight_around))
        select_g = select_griffin(g_all) #选怪兽
        skill = randint(1,10)    #随机选取技能
        print(skill)
        if skill <=6:
            print("%s 使用普通攻击打 %s"% (u.name,select_g.name))
            print(select_g)
            u.attack(select_g)   #普通攻击打击怪兽，扣血
            print("%s 恢复了 %d 魔法值" % (u.name,u.magic_recover()))  #每回合提升魔法值
        elif skill <=9 :
            if u.magic_attack(g_all):
                print("%s 使用魔法攻击"% (u.name))
            else:
                print("%s 使用普通攻击打 %s"% (u.name,select_g.name))
        else:
            if u.unique_attack(select_g)>0:
                print("%s 使用必杀技攻击 %s"% (u.name,select_g.name))
        
        if select_g.alive>0:
            select_g.attack(u)
            print("%s 回击 %s" % (select_g.name,u.name))
        
        display_show(u,g_all)
        fight_around +=1
    ###############战斗结束#######################
    if u.alive > 0:
        print('%s win !!!' % (u.name))
    else:
        print("怪兽们胜利了!!!")

if __name__ =='__main__':
    main()

"""
bug :   1.类型错误:不支持操作数类型-=:'str'和'int' 错误原因：在进行装饰器setter时使用的方法名是name,而不是hp

本次代码的总结：
1）逻辑较为混乱，写着写着就把变量模糊了

"""

