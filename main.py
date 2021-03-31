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