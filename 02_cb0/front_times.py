def front_times(str, n):
  result = ''
  while n != 0:
	result = result + str[0: 3]
	n -= 1
  return result

