def arithmetic_arranger(problems , show_sol = False):
  # check the number of problems
  if (len(problems) > 5) :
    return "Error: Too many problems."

  first_operand = []
  operator = []
  second_operand = []

  for problem in problems:
    pieces = problem.split()
    first_operand.append(pieces[0])
    operator.append(pieces[1])
    second_operand.append(pieces[2])

  # check for * or / in operator
  if '*' in operator or '/' in operator:
    return "Error: Operator must be '+' or '-'."

  # check the digits
  for i in range(len(first_operand)):
    if not(first_operand[i].isdigit() and second_operand[i].isdigit()):
      return "Error: Numbers must only contain digits."

  # check for the length of operand
  for i in range(len(first_operand)):
    if (len(first_operand[i]) > 4 or len(second_operand[i]) > 4):
      return "Error: Numbers cannot be more than four digits."


  first_l = []
  second_l = []
  third_l = []
  fourth_l = []

  # for the first_l 
  
  for i in range(len(first_operand)):
    if(len(first_operand[i]) > len(second_operand[i])):
      first_l.append(" " * 2 + first_operand[i])
    else:
      first_l.append(" " * (len(second_operand[i]) - len(first_operand[i]) + 2) + first_operand[i])
  
  #for the second_l
  
  for i in range(len(second_operand)):
    if(len(second_operand[i]) > len(first_operand[i])):
      second_l.append(operator[i] + " " + second_operand[i])
    else:
      second_l.append(operator[i] + " " * (len(first_operand[i]) - len(second_operand[i]) + 1) + second_operand[i])

  # for the third_l

  for i in range(len(first_operand)):
    third_l.append("-" * (max(len(first_operand[i]) , len(second_operand[i])) + 2))

  # for the fourth_l & ans
  for i in range(len(first_operand)):
    if operator[i] == "+":
      ans = str(int(first_operand[i]) + int(second_operand[i]))
    else:
      ans = str(int(first_operand[i]) - int(second_operand[i]))

    if (len(ans) > max(len(first_operand[i]) , len(second_operand[i]))):
      fourth_l.append(" "+ans)
    else:
      fourth_l.append(" " * (max(len(first_operand[i]) , len(second_operand[i])) - len(ans) + 2) + ans)


  # Displaying the solution
  if show_sol:
    arranged_problems = (" "*4).join(first_l) + "\n" + (" "*4).join(second_l) + "\n" + (" "*4).join(third_l) + "\n" + (" "*4).join(fourth_l)
  else:
    arranged_problems = (" "*4).join(first_l) + "\n" + (" "*4).join(second_l) + "\n" + (" "*4).join(third_l)
    
  return arranged_problems