def turnLeft():
  if(roverPosition[2] > 0):
    roverPosition[2] = roverPosition[2] - 1
  else:
    roverPosition[2] = 3

def turnRight():
  roverPosition[2] = (roverPosition[2] + 1) % 4

def moveForward():
  if(roverPosition[2] == 0):
    roverPosition[1] = roverPosition[1] + 1
  elif(roverPosition[2] == 1):
    roverPosition[0] = roverPosition[0] + 1
  elif(roverPosition[2] == 2):
    roverPosition[1] = roverPosition[1] - 1
  elif(roverPosition[2] == 3):
    roverPosition[0] = roverPosition[0] - 1


def printOutput():
  x = str(roverPosition[0]) 
  y = str(roverPosition[1])
  print("Output")
  print( x  + ' ' +  y + ' ' + headings[roverPosition[2]])

if __name__ == '__main__':
  
  plateauGrid=[[]]
  # headings = ['N', 'E', 'S', 'W']
  headings = dict([(0, 'N'), (1, 'E'), (2, 'S'), (3, 'W')])

  print("Please enter the upper-right coordinates of the plateau")
  coordinates = list(map(int, input().split()))

  print("Enter rovers position")
  roverPosition = input().split()

  roverPosition[0] = int(roverPosition[0])
  roverPosition[1] = int(roverPosition[1])

  for x in headings:
    if(headings[x] == roverPosition[2]):
      roverPosition[2] = x

  print("Enter the series of instructions for the rover how to explore the plateu")
  instructions = list(input())

  for inst in instructions:
    if(inst == 'M'):
      moveForward()
    elif(inst == 'L'):
      turnLeft()
    elif(inst == 'R'):
      turnRight()

  printOutput()