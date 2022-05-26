def fibonacci(n):
  holder = [1]
  next_number = 1
  fib = [1, 1]

  if n == 0:
    return 0
  if n <= 2:
    return 1

  while len(fib) < n:
    holder.append(next_number)
    next_number = next_number + holder[0]
    fib.append(next_number)
    holder.pop(0)
  
  return fib.pop()
