import sys
sys.stdin = open('input.txt', encoding='utf-8')

Man1 = input()
Man2 = input()

# list = ["가위", "바위", "보"]

if Man1 == "바위" and Man2 == "가위":
    print('Result : Man1 Win!')
elif Man1 == "바위" and Man2 == "보":
    print('Result : Man2 win!')
elif Man1 == "가위" and Man2 == "바위":
    print('Result : Man2 win!')
elif Man1 == "가위" and Man2 == "보":
    print('Result : Man1 win!')
elif Man1 == "보" and Man2 == "가위":
    print('Result : Man2 win!')
elif Man1 == "보" and Man2 == "바위":
    print('Result : Man1 win!')
else:
    print('Result : Draw!')


# 가위=0, 바위=1, 보=2

# 가위 (바위) win2 
# (가위) 보   win1
# 바위 (보)   win2
# (바위) 가위 win1
# 보 (가위)   win2
# (보) 바위   win1