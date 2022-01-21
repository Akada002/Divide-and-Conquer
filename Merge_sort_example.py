def merge_sort(elements,key,decending=False):
  if len(elements)<=1:
    return elements
  size = len(elements)//2
  left_list = merge_sort(elements[:size],key,decending)
  right_list = merge_sort(elements[size:],key,decending)
  sorted_list = merge(left_list,right_list,key,decending)
  return sorted_list

def merge(left,right,key,decending):
  merged=[]
  if decending:
    while len(left)>0 and len(right)>0:
      if left[0][key]>= right[0][key]:
        merged.append(left.pop(0))
      else:
        merged.append(right.pop(0))

  else:
    while len(left)>0 and len(right)>0:
      if left[0][key]<=right[0][key]:
        merged.append(left.pop(0))
      else:
        merged.append(right.pop(0))

  merged.extend(left)
  merged.extend(right)
  return merged


if __name__ == '__main__':
    elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]
    sorted_list = merge_sort(elements,key='time_hours',decending=False)
    print(sorted_list)
