def most_frequent_digits(numbers_string):
  digits_count = {}
  for digit in numbers_string:
    if digit in '0123456789':
      if digit in digits_count:
        digits_count[digit] += 1
      else:
        digits_count[digit] = 1
  sorted_count = {k: v for k, v in sorted(digits_count.items(), key = lambda x: x)}
  return sorted_count

# Test the function
input_number_string = '123321'
print(most_frequent_digits(input_number_string))