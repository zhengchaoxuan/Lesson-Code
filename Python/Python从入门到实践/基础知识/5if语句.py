# 该代码是python从入门到实践的练习源码
# date ：2020/07/19
# version :0.1
# including:
# 1.关键字--in 和 not in 
# 2.确定列表不为空
#5-3
alien_color = 'greens'
if alien_color =='green':
    print('you win the 5 scores')
elif alien_color =='red':
    print('you win the 10 scores')
else:
    print('you win the 15 scores')

#5-7
alien_colors = ['green','red','greens']
if alien_color in alien_colors:
    print('you win the 10 scores')

#5-8
admins = ['admin','wz','wqd','cxk','pyy']
if admins: #判断是否为空
    if 'admin' in admins:
        print('Hello admin would you like to see a status report?')
    else:
        print("hello,Eric,thank you for logging in again")
else:
    print("we need to  find some users")

#5-10
print('\n')
current_users = ['zcx','wz','wqd','cxk','pyy']
new_users = ['zcx','wmt','qyl','hxt','zbm']
for new_user in new_users:
    if new_user.lower() in current_users:
        print('please enter other name!')
    else:
        print('the name not be used!')

#5-11
print('\n')
lists = list(range(1,10))
for list1 in lists:
    if list1 == 1:
        print(str(list1)+'st')
    elif list1 == 2:
        print(str(list1)+'nd')
    elif list1 == 3:
        print(str(list1)+'rd')
    else:
        print(str(list1)+'th')






