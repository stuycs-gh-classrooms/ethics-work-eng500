def string_splosion(str):
  n = 0
  result = ''
  while n < len(str):
	result += str[0:n + 1]
	n += 1
  return result

