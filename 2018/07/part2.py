import re

prereqs = {}
done = []
time = 0
elf_jobs = ['.'] * 5
elf_time = [0] * 5

def do_tick():
  global time
  global elf_jobs
  global elf_time

#  print('{}: {} {} {} {} {} | {}'.format(time, 
#    elf_jobs[0], elf_jobs[1], elf_jobs[2],
#    elf_jobs[3], elf_jobs[4], ''.join(done)))

  # update elves
  for i in range(5):
    elf_time[i] -= 1
    if elf_time[i] == 0:
      for y in prereqs.items():
        if elf_jobs[i] in y[1]: 
          y[1].remove(elf_jobs[i])
      done.append(elf_jobs[i])
      elf_jobs[i] = '.'

  time += 1

def try_dispatch(job):
  global elf_jobs
  global elf_time

  reqtime = 60 + (ord(job) - ord('A') + 1)
  for i in range(5):
    if elf_jobs[i] == '.':
#      print('Dispatched job {} to elf #{}'.format(job, i))
      elf_jobs[i] = job
      del prereqs[job]
      elf_time[i] = reqtime
      return
  
#  print('Unable to dispatch job {}, all elves busy...'.format(job))

def elves_still_working():
  for i in range(5):
    if elf_jobs[i] != '.': return True

  return False  

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

while prereqs or elves_still_working():
  possible_steps = [x[0] for x in prereqs.items() if len(x[1])==0]
  possible_steps.sort()

  for st in possible_steps:
    try_dispatch(st)

  do_tick()

print(time)

