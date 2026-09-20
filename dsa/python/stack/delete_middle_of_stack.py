stack=[5,4,3,2,1]
list=[]
while stack:
  x=stack.pop()
  list.append(x)

list.sort(reverse=True)
n=(len(list)/2)+1
list.remove(n)


