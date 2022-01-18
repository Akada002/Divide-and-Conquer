
def merge_sort(arr):
  if len(arr)<=1:
    return arr
    
  mid = len(arr)//2
  left = arr[:mid]
  right = arr[mid:]

  merge_sort(left)
  merge_sort(right)

  return Merge_sort_two_array(left, right, arr)
def Merge_sort_two_array(A,B, arr):
  a=len(A)
  b=len(B)
  i=j=k=0
  sorted_array=[]
  while i<a and j<b:
    if A[i]<B[j]:
      arr[k]=A[i]
      i+=1
    else:
      arr[k]=B[j]
      j+=1
    k+=1
  while i<a:
    sorted_array.append(A[i])
    i+=1
    k+=1
  while j<b:
    sorted_array.append(B[j])
    j+=1
    k+=1


if __name__ == "__main__":
  Arr=[29,2,40,3,50,47,23,98,80,100,189]
  merge_sort(Arr)
  print(Arr)
