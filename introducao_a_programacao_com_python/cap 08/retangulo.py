def rectangle(width, height, char="*"):
  row = char * width

  for i in range(height):
    print(row)

rectangle(3, 4)
rectangle(9, 5)
rectangle(12, 12, "o")
