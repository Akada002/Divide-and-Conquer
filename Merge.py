A = [22,23, 26, 40, 56, 80,100,189]
B = [2, 19, 48, 54,55, 66]
C = []

def Merge_Sort(A, B):
  i=j=0
  while i < len(A) and j < len(B):
    if A[i] <= B[j]:
      C.append(A[i])
      i += 1

    else:
      C.append(B[j])
      j += 1
  while i< len(A):
    C.append(A[i])
    i+=1
  while j< len(B):
    C.append(B[j])
    j+=1
  
  return C


print(Merge_Sort(A, B))

________________________________________________

def merge_sort(a,b):
  sorted_list=[]
  i=j=0

  while i<len(a) and j<len(b):
    if a[i]>= b[j]:
      sorted_list.append(a[i])
      i+=1
    else:
      sorted_list.append(b[j])
  while i< len(a):
    sorted_list.append(a[i])
    i+=1
  while j< len(b):
    sorted_list.append(b[j])
    j+=1
  return sorted_list

if __name__ == '__main__':
  a=[5,8,12,56]
  b=[7,9,45,51]

  print(merge_sort(a,b))
