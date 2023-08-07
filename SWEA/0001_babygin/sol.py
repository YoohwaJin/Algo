import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    numbers = input() # 맨 앞의 0이 사라지는걸 막기 위해 문자로 저장
    counter = [0 for _ in range(10)] # 0이 10개가 차있는 리스트 생성

    for number in numbers:
        counter[int(number)] += 1 # [0, 0, 0, 0, 0, 0, 3, 3, 0 ] 이런식으로 출력
    
    # print(counter) # 프린트 위치에따라 전체 과정을 출력하기도 하고, 첫번째 인풋만 출력하기도 **주의

    idx = 0
    is_babygin = 0

    while idx < len(counter):

        # 1. 트리플인지 검증
        if counter[idx] >= 3:
            counter[idx] -= 3
            is_babygin += 1

        # 2. run(straight)인지 검증
        if idx < len(counter) -2: #0-9까지 있지만, 789가 최대 런이기 때문에 8, 9 이상으로는 볼 필요가 없음
            if counter[idx] and counter[idx+1] and counter[idx+2]: #기준 숫자 오른쪽으로 계속해서 1(존재)이라면 run
                is_babygin += 1
                counter[idx] -= 1
                counter[idx+1] -= 1
                counter[idx+2] -= 1

        idx += 1

    if is_babygin == 2:
        print(f'#{tc}True')
    else:
        print(f'#{tc}Flase')


        



# 6개의 숫자 중 중복되는 값이 6개이면 *if(min(numbers) == max(numbers))
# true 출력
# 6개의 숫자 중 중복되는 값이 3개이면(리스트 인자를 크기순서로 나열했을 때, index 0과 index 2가 일치)
#     나머지 3개 숫자가 같은 경우 true 
#     나머지 3개 숫자가 연속될 경우 true
# 6개의 숫자가 모두 연속되는 경우 
# true 출력
# 6개의 숫자 중 3개가 연속될 경우
#     나머지 3개 숫자가 연속될 경우 true
    
#     else False
