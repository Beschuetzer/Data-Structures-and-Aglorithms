import random, json, os

def create_numbers_list(size, min, max, isFloat = False):
  numbers = []
  for i in range(size):
    if isFloat: numbers.append(min + (random.random() * max))
    else: numbers.append(random.randint(min, max))
  return numbers

def write_to_file(data, filename, location = ''):
  with open(f"{location}{filename}", "w") as f:
    json.dump(data, f)

def load_file(filename, location=''):
  with open(f"{location}{filename}", 'r') as f:
    return json.load(f)

def selection_sort(values):
  sorted_list = []
  for i in range(0, len(values)):
    index_to_move = index_of_min(values)
    sorted_list.append(values.pop(index_to_move))
  return sorted_list

def index_of_min(values):
  min_index = 0
  for i in range(1, len(values)):
    if values[i] < values[min_index]:
      min_index = i
  return min_index

numbers = None
if os.path.exists('./numbers-10k.json'): 
  print('loading...')
  numbers = load_file('numbers-10k.json')
else: numbers = create_numbers_list(10000, 0, 100, True)
# print('numbers = {0}'.format(numbers))

# dict = None
# if os.path.exists: dict = load_file('test.json')
# print('dict["test"] = {0}'.format(dict['test']))
# write_to_file({"test": 123, "test2": 321}, 'test.json')

# numbers = create_numbers_list(1000, 0, 100, True)
# write_to_file(numbers, 'numbers-1k.json')

# print(selection_sort(numbers))
# print('sorted = {0}'.format(sorted))