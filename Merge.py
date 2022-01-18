A = [22, 26, 40, 56, 80]
B = [2, 19, 48, 54, 66]
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
  return C


print(Merge_Sort(A, B))
