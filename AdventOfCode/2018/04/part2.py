import re

guard_by_day = {}
sleeptime_by_day = {}
sleeptime_by_guard = {}
guards = []

with open('input.txt', mode='r') as f:
  lines = sorted(f.readlines())

  active_guard = 0
  sleep_start_min = 0
  sleep_end_min = 0
  sleeptime = []
  current_day = ''

  for line in lines:
      m = re.match('\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\]', line)
      (year, month, day) = (int(m.groups()[0]), int(m.groups()[1]), int(m.groups()[2]))
      (hour, minute) = (int(m.groups()[3]), int(m.groups()[4]))

      action = line.rstrip()[19:]

      if action=='wakes up':
        sleep_end_min = int(minute)
        sleeptime_by_guard[active_guard] += sleep_end_min - sleep_start_min
        for i in range(sleep_start_min, sleep_end_min):
          sleeptime[i] = 1
        sleeptime_by_day[current_day] = sleeptime.copy()
      elif action=='falls asleep':
        guard_by_day['{}-{}-{}'.format(year, month, day)] = active_guard
        sleep_start_min = int(minute)
        current_day = '{}-{}-{}'.format(year, month, day)
      else:
        m = re.match('Guard #(\d+) begins shift', action)
        active_guard = int(m.groups()[0])
        if active_guard not in guards:
          guards.append(active_guard)

        sleeptime = [0] * 60
        if active_guard not in sleeptime_by_guard:
          sleeptime_by_guard[active_guard] = 0

maxima = {}

for guard in guards:
  histogram = [0] * 60
  # build histogram for that guard
  for day in sleeptime_by_day.keys():
    if guard_by_day[day] == guard:
      histogram = [ sum(x) for x in zip(histogram, sleeptime_by_day[day]) ]

  maxvalue = max(histogram)
  maxindex = histogram.index(maxvalue)
  maxima[maxvalue] = (guard, maxindex)
  # print('Guard {}: slept {} times at minute {}'.format(guard, maxvalue, maxindex))

maxcount = max(maxima)
(maxguard,maxminute) = maxima[maxcount]

print('{} * {} = {}'.format(maxguard, maxminute, maxguard * maxminute))

