#corey b. holstege
#2018-09-10
#https://courses.edx.org/courses/course-v1:GTx+CS1301xI+1T2018/courseware/4d3eee72814e4f3a9d3147a0cec4be39/ad6437e6249349ffb67273b1d60e865d/1?activate_block_id=block-v1%3AGTx%2BCS1301xI%2B1T2018%2Btype%40vertical%2Bblock%409c7f8004828f4d02b130c38ad35253d4

#countdown function
#prints the numbers from 1 to i
#on a single line
def countdown(i):
	for j in range(1, i + 1):
		print(j, end = " ")
	print()
countdown(10)
countdown(5)
countdown(2)