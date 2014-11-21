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
# List of jobs
job_queue = []  
with open( sys.argv[1], 'r' ) as f:
  for line in f:
    job = Job()
    line = line.split()
    job.name = line[0]
    job.start = int( line[1] )
    job.finish = int( line[2] )
    job_queue.append(job)
# Sort the jobs by finish time
job_queue.sort(key=lambda obj: obj.finish)
sched = earliest_finish_time(job_queue)
for job in sched:
  print(job.name)