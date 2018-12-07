import re

prereqs = {}
done = []

with open('input.txt', mode='r') as f:
  lines = f.readlines()

  for line in lines:
    m = re.match('Step (.) must be finished before step (.) can begin', line)

    step = m.groups()[1]
    prereq = m.groups()[0]

    if step not in prereqs:
      prereqs[step] = []
    if prereq not in prereqs:
      prereqs[prereq] = []

    prereqs[step].append(prereq)

while prereqs:
  possible_steps = [x[0] for x in prereqs.items() if len(x[1])==0]
  possible_steps.sort()

  next_step = possible_steps[0]

  done.append(next_step)

  # remove from all prereqs
  for y in prereqs.items():
    if next_step in y[1]: 
      y[1].remove(next_step)

  # remove the entries themselves from the todo-list  
  del prereqs[next_step[0]]

print(''.join(done))
  

