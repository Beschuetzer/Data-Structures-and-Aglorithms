import unittest, merge_sort, random, time
from unittest import result


def getRandomList(size):
  result = []
  rangeMax = 10**2
  print('range = {0}'.format(range))
  for i in range(size):
    randomInt = random.randrange(0, rangeMax, 1)
    result.append(randomInt)

  return result

randomList = getRandomList(10000)
sortedRandomList = sorted(randomList, reverse=False)

class own_merge_sort(unittest.TestCase):
  def setUp(self) -> None:
      self.startTime = time.time()
  def tearDown(self) -> None:
      print(f'Time: {time.time() - self.startTime}')
      print('self.list = {0}'.format(self.list))
      print('self.actual = {0}'.format(self.actual))
      print('self.expected = {0}'.format(self.expected))

  def test_none(self):
    self.list = []
    self.actual = merge_sort.merge_sort(self.list)
    self.expected = []
    self.assertListEqual(self.actual, self.expected)
  def test_one(self):
    self.list = [9, 4]
    self.actual = merge_sort.merge_sort(self.list)
    self.expected = [4,9]
    self.assertListEqual(self.actual, self.expected)
  def test_three(self):
    self.list = [9, 4, 1]
    self.actual = merge_sort.merge_sort(self.list)
    self.expected = [1,4,9]
    self.assertListEqual(self.actual, self.expected)
  def test_four(self):
    self.list = [9, 4, 1]
    self.actual = merge_sort.merge_sort(self.list)
    self.expected = [1,4,9]
    self.assertListEqual(self.actual, self.expected)
  def test_same(self):
    self.list = [9, 1, 9, 1,9,2,4,7,4,9]
    self.actual = merge_sort.merge_sort(self.list)
    self.expected = sorted(self.list, reverse=False)
    self.assertListEqual(self.actual, self.expected)
  def test_failed_once_upon_a_time(self):
    self.list = [0, 3, 4, 2, 1, 3, 1, 2, 3, 4]
    self.actual = merge_sort.merge_sort(self.list)
    self.expected = [0, 1, 1, 2, 2, 3, 3, 3, 4, 4]
    self.assertListEqual(self.actual, self.expected)

  def test_random(self):
    self.list = randomList
    self.actual = merge_sort.merge_sort(self.list)
    self.expected = sortedRandomList
    self.assertListEqual(self.actual, self.expected)


class example_merge_sort(unittest.TestCase):
  def setUp(self) -> None:
      self.startTime = time.time()
  def tearDown(self) -> None:
      print(f'Time: {time.time() - self.startTime}')
      print('self.list = {0}'.format(self.list))
      print('self.actual = {0}'.format(self.actual))
      print('self.expected = {0}'.format(self.expected))

  def test_none(self):
    self.list = []
    self.actual = merge_sort.merge_sort_example(self.list)
    self.expected = []
    self.assertListEqual(self.actual, self.expected)
  def test_one(self):
    self.list = [9, 4]
    self.actual = merge_sort.merge_sort_example(self.list)
    self.expected = [4,9]
    self.assertListEqual(self.actual, self.expected)
  def test_three(self):
    self.list = [9, 4, 1]
    self.actual = merge_sort.merge_sort_example(self.list)
    self.expected = [1,4,9]
    self.assertListEqual(self.actual, self.expected)
  def test_four(self):
    self.list = [9, 4, 1]
    self.actual = merge_sort.merge_sort_example(self.list)
    self.expected = [1,4,9]
    self.assertListEqual(self.actual, self.expected)
  def test_same(self):
    self.list = [9, 1, 9, 1,9,2,4,7,4,9]
    self.actual = merge_sort.merge_sort_example(self.list)
    self.expected = sorted(self.list, reverse=False)
    self.assertListEqual(self.actual, self.expected)
  def test_failed_once_upon_a_time(self):
    self.list = [0, 3, 4, 2, 1, 3, 1, 2, 3, 4]
    self.actual = merge_sort.merge_sort_example(self.list)
    self.expected = [0, 1, 1, 2, 2, 3, 3, 3, 4, 4]
    self.assertListEqual(self.actual, self.expected)

  def test_random(self):
    self.list = randomList
    self.actual = merge_sort.merge_sort_example(self.list)
    self.expected = sortedRandomList
    self.assertListEqual(self.actual, self.expected)





