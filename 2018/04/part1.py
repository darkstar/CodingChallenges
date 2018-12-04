import re

guard_by_day = {}
sleeptime_by_day = {}
sleeptime_by_guard = {}

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
        sleeptime = [0] * 60
        if active_guard not in sleeptime_by_guard:
          sleeptime_by_guard[active_guard] = 0

# find our sleepyhead
sleepy_guard = max(sleeptime_by_guard, key = lambda key: sleeptime_by_guard[key])

histogram = [0] * 60

# find all days where he has duty
for day in guard_by_day.keys():
  if guard_by_day[day] == sleepy_guard:
    # Add the day's sleep table onto the histogram
    histogram = [ sum(x) for x in zip(histogram, sleeptime_by_day[day]) ]

# get the index of the fist (assumed: only) maximum of the histogram
sleepiest_minute = histogram.index(max(histogram))

print('{} * {} = {}'.format(sleepy_guard, sleepiest_minute, sleepy_guard * sleepiest_minute))

