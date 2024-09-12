# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# recursive
def generate_parentheses(n):
  if n == 0:
    return []

  result = []
  def generate(current, open_count, closed_count):
    if open_count == n and closed_count == n:
      result.append(current)
      return

    if open_count < n:
      generate(current + '(', open_count + 1, closed_count)
    if closed_count < open_count:
      generate(current + ')', open_count, closed_count + 1)
    
  generate('', 0, 0)
  return result

print(generate_parentheses(4))