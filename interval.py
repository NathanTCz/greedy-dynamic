import sys

# Greedy Scheduling algorithm for earliest finish
# time first
def earliest_finish_time (jobs):
  sched = []
  sched.append( jobs[0] )

  k = 0
  for i in range(1, len(jobs) ):
    if jobs[i].start >= jobs[k].finish:
      sched.append( jobs[i] )
      k = i

  return sched

class Job:
  name = ''
  start = int()
  finish = int()

  def __init__(self, n, s, f):
    self.name = n
    self.start = int(s)
    self.finish = int(f)

# List of jobs
job_queue = []

with open( sys.argv[1], 'r' ) as f:
  for line in f:
    line = line.split()
    job = Job( line[0], line[1], line[2] )
    job_queue.append(job)

# Sort the jobs by finish time
job_queue.sort(key=lambda obj: obj.finish)

sched = earliest_finish_time(job_queue)

for job in sched:
  print(job.name)
