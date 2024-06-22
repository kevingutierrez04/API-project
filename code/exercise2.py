# WRITE YOUR CODE HERE
def move_to_bottom(d,k):
#returns dict where key/value are moved to move_to_bottom
#if key not in dict, return str
  if k in d:
    temp = d.get(k)
    del d[k]
    d[k] = temp
    return d
  else:
    e = "The key is not in the dictionary"
    return e

# test code below
if __name__ == "__main__":
  example_dict = {
    1 : 'one',
    2 : 'two',
    3 : 'three'
  }

  move_to_bottom(example_dict, 4)
  print(example_dict)