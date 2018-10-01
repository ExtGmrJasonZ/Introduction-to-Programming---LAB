arr = ([1, 2, 3, 4, 5, 6, 7])               #This is the array "arr"

Ar = arr[1::-1]                             #Variable Ar is when I reverse the array using slicing from only index 0 to index 1
Br = arr[:1:-1]                             #Variable Br is when I reverse the array using slicing after index 1 until the final index
print(Ar, Br, Br [::-1] + Ar[::-1])         #I want to print Ar, Br, and Br reversed and Ar reversed
