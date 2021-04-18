a=[2,4,4,3,7,8,7,1,2,1]

#calculating count array
count = [0] * len(a)
for i in range(len(a)):
    count[a[i]] += 1
print(count)

#calcultaing cumulative count
for i in range(len(a)):
    count[i] += count[i - 1]
print(count)

output=[0]* len(a)
i = len(a) - 1
while i >= 0:
    output[count[a[i]] - 1] = a[i]
    count[a[i]] -= 1
    print(count[a[i]])
    i -= 1

# Copy the sorted elements into original array
for i in range(len(a)):
    a[i] = output[i]
print(a)


    
