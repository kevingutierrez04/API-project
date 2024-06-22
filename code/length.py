def pop_item(d):
  if len(d) == 0:
    return -1
  else:
    return d.popitem()

watches = {}

print(pop_item(watches))