elements=[78,12,15,8,61,53,23,27]
size=len(elements)
for i in range(size-1):
    min_index=i
    for j in range(i+1,size):
        if elements[j]<elements[min_index]:
            min_index=j
    if i != min_index:
        elements[i],elements[min_index]=elements[min_index],elements[i]
print("sorted list:",elements)
