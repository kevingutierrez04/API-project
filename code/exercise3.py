# WRITE YOUR CODE HERE
def swap(d):
  #returns d where k and v are swapped
  #if unhashable value, return str
  def hashable(v):
    try:
      hash(v)
    except TypeError:
      return False
    return True
  d2 = {
  }

  for k,v in d.items():
    if hashable(v) == False:
      s = "Cannot swap the keys and values for this dictionary"
      return s
    d2[v] = k
  return d2


# test code below
# test code below
if __name__ == "__main__":
  example_dict = {
    1 : 'one',
    2 : 'two',
    3 : (4, 5)
  }

  swapped = swap(example_dict)
  print(swapped)