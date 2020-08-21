# 该代码是python从入门到实践的练习源码
# date ：2020/07/19
# version :0.1
# including:
#1.列表之间的移动元素
#2.remove函数配合while进行删除特定元素
#3.input进行字典输入

#练习：列表之间的移动元素--未验证的用户转到验证完的用户
unconfirmed_users = ['zcx','wmt','wqd']
confirmed_users=[]
while unconfirmed_users: #判断是否还有未验证的用户
    ##验证的代码无（假设验证完）
    newconfirmed_user = unconfirmed_users.pop(0) #从列表第一个验证
    confirmed_users.append(newconfirmed_user)
print(confirmed_users)


# 7-1
car = input('please enter you want to rent the car: ')
print('Let me see if I can find you a '+car)

# 7-2
customer_number = input('please enter the number of customer: ')
customer_number = int(customer_number) #输出的是字符
if customer_number>8:
    print('we have not enough table!')
else:
    print('welcome to our restaurant!') 

# 7-3
number = input('please enter a number: ')
number = int(number)
if number%10==0:
    print(str(number)+'是10的整数！')
else:
    print(str(number)+'不是10的整数！')

# 7-4
burden = ''
burdens =[]
while burden!='quit':
    burden = input('enter the burden: ')
    if burden!='quit':
        burdens.append(burden)
        print('we will add the '+burden+"enter our food")
print(burdens)
print('\n')

#7-5 电影票
message = 'enter your age,we gather different price in different age :'
while True:
    customer_age = input(message)
    if customer_age == 'quit':
        break
    elif customer_age.isdigit()==1 and int(customer_age)>0:
        customer_age = int(customer_age)
        if customer_age<3:
            print('it is free')
        elif customer_age<=12:
            print('you should pay 10 dollar!')
        elif customer_age>12:
            print('you should pay 15 dollar!')
    else:
        customer_age = input('enter error,please enter a right age:')

# 7-8 熟食店 --元素转移
sandwich_orders = ['a','b','c','d']
finished_sandwichs=[]
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f'I made you {sandwich} sandwich')
    finished_sandwichs.append(sandwich)
print(finished_sandwichs)

#7-9 特定元素重复的移除
sandwich_orders = ['a','b','a','b','c']
#第一种方法
'''
for sandwich in sandwich_orders:
    if (sandwich =='a'):
        sandwich_orders.remove('a')
print(sandwich_orders)
'''
#书中的方法
while 'a' in sandwich_orders: #判断sandwich_orders是否含有'a'
    sandwich_orders.remove('a')
print(sandwich_orders)

#7-10 居民调查--梦想的度假胜地
surveys ={}
print('if you could visit one place in the world ,where would you go?')
while True:
    name = input("enter your name: ")
    place = input('enter you want to visit place: ')
    surveys[name] = place
    repeat = input('would you want to do this again(yes/no)? ')
    if (repeat.lower()=='yes' or repeat.lower()=='no'):
        if repeat.lower()=='no':
            break
        elif repeat.lower() =='yes':
            continue
    else:
        repeat =input('enter error, please enter again(yes/no): ')
    
print(' ---surveys answer--- ')
for name,place in surveys.items():
    print(name+' : '+ place)






