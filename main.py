import numpy as np
import matplotlib.pyplot as plt
k = int(input("Order of curve 'k' :"))
n = int(input("No. Of control points 'n' :"))

# Defining knot vector i.e x
knot_vector = []
for x in range(0, n+k+1,1):
    knot_vector.append(x)
print(knot_vector)

# 1st order
# 1st create a zero's matrix for n11, n21, n31, n41, n51, n61

N1 = np.zeros((len(knot_vector)-1, 1))
print("matrix of 1st order:",N1)

y = 0
t = 0
parameter_t = np.array()

for i in range(0, (n+k)*2):
    print("previous value of t :",t)
    if knot_vector[y] <= t < knot_vector[y+1]:
        N1[0,0] = 1
        print(N1)
        # plt.plot(t, N1)
        # plt.show()
    # if knot_vector[y+1] <= t < knot_vector[y+2]:
    #     N1[1,0] = 1
    # if knot_vector[y+2] <= t < knot_vector[y+3]:
    #     N1[2,0] = 1
    # if knot_vector[y+3] <= t < knot_vector[y+4]:
    #     N1[3,0] = 1
    # if knot_vector[y+4] <= t < knot_vector[y+5]:
    #     N1[4,0] = 1
    # if knot_vector[y+5] <= t < knot_vector[y+6]:
    #     N1[5,0] = 1
    t += 0.5
    parameter_t.append(t)

    # print("New value of t :",t)

    # print(N1)

plt.plot(parameter_t, N1)
plt.show()
# quiz
# my_list = [4,5,6]
# my_list = my_list.insert(100, '!')
# print(my_list)
