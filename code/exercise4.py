# WRITE YOUR CODE HERE
def is_nested(d):
  for v in d.values():
    if isinstance(v, (dict,list,tuple)):
      return True
  return False

# test code below
if __name__ == "__main__":
  example_dict = {
    1 : 'one',
    2 : {3 : 4},
    5 : 'five'
  }

  print(is_nested(example_dict))