# -*- coding: utf-8 -*-
# @Time    : 2022/10/10 23:24
N = 4
Lights = list(map(int, "50 70 20 70".split()))
res = []
LightSum = 0
for i in range(N):
	left = max(0, 100*i-Lights[i])
	right = min((N-1)*100, 100*i+Lights[i])
	while len(res) > 0 and res[-1][1] > left:
		left_new, right_rew = res.pop(len(res)-1)
		LightSum -= right_rew - left_new
		left = min(left_new, left)
		right = max(right_rew, right)
	LightSum += right - left
	res.append([left, right])
print((N-1)*100 - LightSum)