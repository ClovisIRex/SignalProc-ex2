import numpy as np
import matplotlib.pyplot as plt

#2
t = np.arange(0, (2 - 0.01), 0.01)
x = np.sin(4 * np.pi * t + np.pi/2)
plt.plot(t, x)
plt.title("sin(4pi*t + pi/2)")
plt.xlabel("time")
plt.ylabel("sample")
plt.show()

t = np.arange(0, (2 - 0.01), 1/3)
x = np.sin(4 * np.pi * t + np.pi/2)
plt.plot(t, x)
plt.title("sin(4pi*t + pi/2) second sample")
plt.xlabel("time")
plt.ylabel("sample")
plt.show()


#3

t = np.arange(0, 2, 0.01)
x = np.sin(8 * np.pi * t + np.pi/4)
plt.plot(t, x)
plt.title("sin(8pi*t + pi/4)")
plt.xlabel("time")
plt.ylabel("sample")
plt.show()


t = np.arange(0, (2 - 0.01), 1/3)
x = np.sin(8 * np.pi * t + np.pi/4)
plt.plot(t, x)
plt.title("sin(8pi*t + pi/4) second sample")
plt.xlabel("time")
plt.ylabel("sample")
plt.show()

# 5
# i
t = np.arange(0, 1, (1/100))
x = 4 + 3 * np.cos(np.pi *t)\
    + 2 * np.cos(2 * np.pi *t)\
    + np.cos(3 * np.pi * t)
plt.plot(t, x)
plt.title("question 5 sample i")
plt.xlabel("time")
plt.ylabel("sample")
plt.show()

# ii
t = np.arange(0, 1, (1/1.5))
x = 4 + 3 * np.cos(np.pi *t)\
    + 2 * np.cos(2 * np.pi *t)\
    + np.cos(3 * np.pi * t)
plt.plot(t, x)
plt.title("question 5 sample ii")
plt.xlabel("time")
plt.ylabel("sample")
plt.show()

# iii
t = np.arange(0, 1, (1/100))
x = 5 + (5 * np.cos(np.pi *t)) + 5 * (1 + np.cos(np.pi *t))
plt.plot(t, x)
plt.title("question 5 sample iii")
plt.xlabel("time")
plt.ylabel("sample")
plt.show()



#
# #1
#
# z = np.arange(0, 11, 2)
# k = np.arange(30, 51, 4)
#
# fig, (ax1, ax2) = plt.subplots(1, 2)
# fig.suptitle('K as a function of Z')
# ax1.plot(z, k)
# ax2.stem(z, k)
#
# for ax in (ax1, ax2):
#     ax.set(xlabel='z', ylabel='k')
# plt.savefig("1.png")
# plt.show()
#
#
# #2
# matrixA = np.array([1, 2, 3, 4, 9, 8, 3, 5, 6]).reshape(3, 3)
# matrixB = np.array([5, 8, 23, 10, 7, 1, 3, 2, 1]).reshape(3, 3)
# matrixC = matrixA + matrixB
# matrixD = matrixA * matrixB
# matrixE = np.transpose(matrixA) + np.transpose(matrixB)
#
#
# #3
#
# a = 4
# for i in range(20):
#     a += 2
# print(a)
#
# #4
# r = np.random.randn(100)
# meanR = np.mean(r)
#
# if meanR > 0.4:
#     print('the mean is larger than 0.4')
# else:
#     print('the mean is lower than 0.4')
#
#
# #5
# time = np.arange(0, 3.2, 0.2)
# randVec_1 = np.random.rand(16)
# randVec_2 = np.random.rand(16)
#
# # plotting the line 1 points
# plt.plot(time, randVec_1, label="randVec_1")
# plt.plot(time, randVec_2, label="randVec_2")
#
# plt.xlabel('time')
# plt.ylabel('vector')
# plt.title('randomVectors as functions of time')
#
# plt.legend()
# plt.savefig("5.png")
# plt.show()
