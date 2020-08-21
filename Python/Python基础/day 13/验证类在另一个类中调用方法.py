"""
lesson 1 : 演示了100个线程向同一个银行账户转账（转入1元钱）的场景

Author : 郑超轩
Date   : 2020.02.28
"""

class Account(object,):

    def __init__(self):
        self._balance = 0
    
    def deposit(self,money):
        """计算存款的余额"""
        new_balance = self._balance + money
        #受理的时间0.1s
        self._balance = new_balance
    
    @property
    def balance(self):
        return self._balance

class AddMonneyThead(object):

    def __init__(self,account,money):
        self._account = account
        self._money   = money
    
    def runs(self):
        self._account.deposit(self._money)
    
def main():
    A = Account()
    for _ in range(10):
        t = AddMonneyThead(A,1)
        t.runs()
        print(t)
    print(A.balance) #10




if __name__ == "__main__":
    main()