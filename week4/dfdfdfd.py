lst = [1,4,6,7,77,93,55,3,99,43]
def search (lst,x):
  count = 0 
  for i in lst:
    if i == x:
      return count
    count  +=1
  return -1



index = search(lst,55)
lst[index] =22
print(lst)

