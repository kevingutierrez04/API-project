import timeit
import sys

num = int(sys.argv[1])
large_list = [i for i in range(num)]
large_dict = dict(zip(large_list, large_list))

def test_dict():
  for i in range(num):
    i in large_dict

def test_list():
  for i in range(num):
    i in large_list

list_time = timeit.timeit(test_list)
dict_time = timeit.timeit(test_dict)

print(f'List time: {list_time}')
print(f'Dictionary time: {dict_time}')