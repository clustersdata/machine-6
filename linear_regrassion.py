input_x = [3,8,9,13,3,6,11,21,1,16]
input_y = [30,57,64,72,36,43,59,90,20,83]
x = 10


x_bar = sum(input_x)/len(input_x)
y_bar = sum(input_y)/len(input_y)

def w1(x_bar,y_bar):
	temp1 = 0
	temp2 = 0
	for i in range(10):
		temp1 += (input_x[i]-x_bar) * (input_y[i]-y_bar)
		temp2 += (input_x[i]-x_bar) * (input_x[i]-x_bar)
	return temp1 / temp2

w1 = w1(x_bar,y_bar)
w0 = y_bar-(w1*x_bar)
y = w0 + (w1*x)

print (''y)
