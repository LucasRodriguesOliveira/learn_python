class Array:
  def __init__(self, class_type):
    self.array = []
    self.c_type = class_type

  def __len__(self):
    return len(self.array)

  def __iter__(self):
    return iter(self.array)

  def __getitem__(self, pos):
    return self.array[pos]

  def is_index_valid(self, index):
    return 0 <= index <= len(self.array)

  def is_equal_instance(self, item):
    if not isinstance(item, self.c_type):
      raise TypeError(f"Invalid Type. item {item} is not of type {self.c_type}")

  def search(self, item):
    self.is_equal_instance(item)

    try:
      return self.array.index(item)
    except ValueError:
      return -1

  def add(self, item):
    if self.search(item) == -1:
      self.array.append(item)

  def remove(self, item):
    self.array.remove(item)

  def sort(self, key=None):
    self.array.sort(key=key)
