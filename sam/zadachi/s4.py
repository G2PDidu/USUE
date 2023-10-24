def mean(*args):
   try:
      return sum(args) / len(args)
   except ZeroDivisionError:
      return 'Error'

# Test code
if __name__ == "__main__":
   print(mean(1, 2, 3))
   print(mean())