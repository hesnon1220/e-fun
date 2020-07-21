import random
import numpy as np

num_count = [0,0,0,0,0,0,0,0,0,0]
dice = [0,1,2,3,4,5,6,7,8,9]
times = 1000000

for repeat_time in range(times):
	num_list = [-1,5,9,7,1,4,-1,6,0,3,8,2]
	
	winner = []
	start = 0

	while True :
		
		if len(winner) == 7 :
			break

		rand_result = sum(random.sample(dice, k=2))%10
		while rand_result == 0 :
			rand_result = sum(random.sample(dice, k=2))%10

		get_num = (start + rand_result)%len(num_list)
		if num_list[get_num] < 0 :
			start = get_num
			continue
		else :
			winner.append(num_list[get_num])
			num_list.pop(get_num)
			start = get_num - 1
	for i in winner:
		num_count[i] += 1

r = [i/times for i in num_count]
print(np.vstack((np.array(dice)[np.argsort(r)],np.array(r)[np.argsort(r)])).T)
print('mean:',np.mean(r),'std:',np.std(r))
