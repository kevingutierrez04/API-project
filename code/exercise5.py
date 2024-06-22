import json
# WRITE YOUR CODE HERE
def compare(f1, f2):
  with open(f1) as epic1:
    data1 = json.load(epic1)
  with open(f2) as epic2:
    data2 = json.load(epic2)
  if len(data1) > len(data2):
    s = "Dictionary 1 is longer than dictionary 2"
  elif len(data1) < len(data2):
    s = "Dictionary 2 is longer than dictionary 1"
  else:
    s = "Dictionary 1 and dictionary 2 have the same length"
  return s

# test code below
if __name__ == "__main__":
  import sys
  
  file1 = sys.argv[1]
  file2 = sys.argv[2]

  print(compare(file1, file2))