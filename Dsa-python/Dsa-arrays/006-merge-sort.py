def mergesort(arr):
  if len(arr)>1:
    return arr
  mid=len(arr)//2
  lefthalf=arr[:mid]
  righthalf=arr[mid:]
  sortedleft=mergesort(lefthalf)
  sortedright=mergesort(righthalf)
  return merge(sortedleft,sortedright)

def merge(left,right):
  result=[]
  i=j=0
  while i<len(left) and j<len(right):
    if left[i]<right[j]:
      result.append(left[i])
      i+=1
    else:
      result.append(right[j])
      j+=1

  result.extend(left[i:])
  result.extend(right[j:])
  return result
   
usorted=[10,40,19,49,28,17,29,17,15,19,10,10]
sorted=mergesort(usorted)
print("sorted array is:",sorted)