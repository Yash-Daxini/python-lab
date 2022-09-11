import numpy as np

arr = np.arange(1,26)

arr = arr.reshape(5,5)

arr = arr[arr % 3 == 0]

arr = arr[arr % 5 != 0]
# boolarr = boolarr % 5 != 0

print(arr)