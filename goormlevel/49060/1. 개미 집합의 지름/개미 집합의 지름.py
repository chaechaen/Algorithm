ant, diameter = map(int, input().split())
point = list(map(int, input().split()))

point.sort()

max_cnt = 0
left = 0

for right in range(ant):
	while point[right] - point[left] > diameter:
		left += 1

	# 현재 구간에 포함되는 개미 수 계산
	curr_cnt = right - left + 1

	if curr_cnt > max_cnt:
		max_cnt = curr_cnt

# 제거해야 하는 개미 최소 수 = 전체 개미 수 - 최대로 남길 수 있는 개미 수
print(ant - max_cnt)