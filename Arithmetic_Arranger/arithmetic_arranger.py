import re

def arithmetic_arranger(problems, solve = False):
  #Error Check: # of problems
  if len(problems) > 5:
    return "Error: Too many problems."
    
  #Empty str to add to after formatting!
  first = ""
  second = ""
  lines = ""
  sumx = ""

  #Error Check: Characters and Operands
  for problem in problems:
    if(re.search("[^\s0-9.+-]",problem)):
      if re.search("[/]", problem) or re.search("[*]", problem):
          return "Error: Operator must be '+' or '-'."
      return "Error: Numbers must only contain digits."

  #Use Split to get each part of problem  
    firstNum = problem.split(" ")[0]
    operator = problem.split(" ")[1]
    secondNum = problem.split(" ")[2]

  #Error Check: Number of Digits  
    if len(firstNum) >= 5 or len(secondNum) >= 5:
      return "Error: Numbers cannot be more than four digits."

    #Store Calculation in sum
    sum = ""
    if (operator == "+"):
      sum = str(int(firstNum) + int(secondNum))
    else:  
      sum = str(int(firstNum) - int(secondNum))

    #Right justify for format
    length  = max(len(firstNum), len(secondNum))+2
    top = str(firstNum).rjust(length)
    bottom = operator + str(secondNum).rjust(length -1)
    line = ""
    res = str(sum).rjust(length)

    #Add dashes!
    for s in range(length):
      line += "-"

    #If last problem, don't add spaces at end
    if problem != problems[-1]:
      first += top + '    '
      second += bottom + '    '
      lines += line + '    '
      sumx += res + '    '
    else:
      first += top 
      second += bottom 
      lines += line 
      sumx += res

  #Put all together
  if solve:
    string = first + "\n" + second + "\n" + lines + "\n" + sumx
  else:
    string = first + "\n" + second + "\n" + lines
  return string
