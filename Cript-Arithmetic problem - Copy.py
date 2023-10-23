import string

def solve_cryptarithmetic(equation):
  """Solve a Cryptarithmetic problem.

  Args:
    equation: A string representing a Cryptarithmetic problem.

  Returns:
    A tuple of the solution, or None if the problem has no solution.
  """

  
  letters = set(equation)

  letter_to_number = {}
  for letter in letters:
    letter_to_number[letter] = None


  solution = None

   for permutation in itertools.permutations(string.digits):

    left_hand_side_sum = 0

        for letter in equation:
      
      if letter not in string.digits:
        left_hand_side_sum += letter_to_number[letter]

    
    if left_hand_side_sum == equation.split('=')[1]:
      solution = permutation

    
    if solution is not None:
      break

  return solution
