def linearsearch(arr,targetvalue):
  for i in range(len(arr)):
    if arr[i]==targetvalue:
      return i
  return -1
arr=[1.4,9,10,18,9,0,8,9,7,2,4,5]
targetvlaue=5
result=linearsearch(arr,targetvalue)
if result!=-1:
  print("value",targetvalue,"found at position",result)
else:
  print("value",targetvalue,"not found")
