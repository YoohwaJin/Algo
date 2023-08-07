import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N = int(input())
    building_list = list(map(int, input().split()))

    # print(N, building_list)

    total = 0
    for i in range(N):
        # print(i, building_list[i])
        now = building_list[i]

        # 현재 위치에 건물이 없다면 다음 건물로 이동
        if now == 0:
            continue

        # 나의 위치에 건물이 있는경우
        else:
            # 양옆 * 2 건물의 높이를 비교
            dx = [-2, -1, 1, 2]

            max_tall = 0

            for j in range(4):
                # i : 현재위치
                # dx[j] : 기준건물을 중심으로 좌우 인덱스
                comp = building_list[i+dx[j]]

                if max_tall < comp:
                    max_tall = comp

            # 나머지 네개의 건물보다 내가 더 크다면 조망권 확보
            if now > max_tall:
                view = now - max_tall
                total += view

    print(f'#{tc} {total}')