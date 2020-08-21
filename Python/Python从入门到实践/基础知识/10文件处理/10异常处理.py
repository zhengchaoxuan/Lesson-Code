# 该代码是python从入门到实践的练习源码
# date ：2020/07/20
# version : 0.1


# 练习1 -- Zero异常
while True:
    first_number = input('enter the number: ')
    if first_number == 'q':
        break
    second_number = input('enter the number: ')
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print('you can not divide by 0')
    else:
        print(answer)

# 练习2 -- 分析文本
file_name = 'D:/Vistual studio editor/Code/Python/Python从入门到实践/基础知识/10文件处理/Python.txt'
try:
    with open(file_name) as file_object:
        content = file_object.read()
except FileNotFoundError:
    print('file not find!')
else:
    list = content.split() # 根据一个字符串创建一个单词列表
    print(list)

# 10-6 加法运算 -- TypeError
while True:
    try:
        number = input('enter a number: ')
        number = int(number)
    except ValueError:
        number = input('please enter a number: ')
    else:
        print(number)
        break


''' 10-6 答案代码''' 
print("Enter 'q' at any time to quit.\n")

while True:
    try:
        x = input("\nGive me a number: ")
        if x == 'q':
            break

        x = int(x)

        y = input("Give me another number: ")
        if y == 'q':
            break

        y = int(y)

    except ValueError:
        print("Sorry, I really needed a number.")

    else:
        sum = x + y
        print("The sum of " + str(x) + " and " + str(y) + " is " + str(sum) + ".")


# 10-7 猫和狗 
cat_names = 'Python从入门到实践/基础知识/10文件处理/cats.txt'
dog_names = 'Python从入门到实践/基础知识/10文件处理/dogs.txt'
try:
    #打开猫的文件
    with open(cat_names) as cats_object:
        cat_name = cats_object.read()

    #打开狗的文件
    with open(dog_names) as dogs_object:
        dog_name = dogs_object.read()
except FileNotFoundError:
    print("we can not find the dog or the cat file!")
    #pass
else:
    print(cat_name)
    print(dog_name)


''' 10-8 答案代码'''  # 使用到了列表,并且不要else因为使用出现异常就会转到异常处理的代码中
filenames = ['Python从入门到实践/10文件处理/cats.txt','Python从入门到实践/基础知识/10文件处理/dogs.txt']
for filename in filenames:
    print("\nReading file: " + filename)
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print("  Sorry, I can't find that file.")


# 常见单词
file_name =  'Python从入门到实践/基础知识/10文件处理/Python.txt'
try:
    with open(file_name) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print('can not find the file_name!')
else:
    Python_number =content.count('Python')
    print(Python_number)

