import sys, time
import jobs

def showJobs(job):
  """
  first, store a timestamp in the variable `now`.  Then, create a new Job object and 
  pass the timestamp in.  Each field in the Job object will be converted to seconds
  and then added to the time stamp to calculate the next time that each job will 
  run.
  """
  now = int(time.time())
  try:
    j = jobs.Job(job)
    j.processJobs(now)
  except IndexError:
    pass

def processlines(line):
  """
  Iterate through each line in the file, ignoring lines that begin with a hash mark,
  and split them on spaces.  Collect each word into a list, pre-process it a little,
  and then call showJobs() on each list.
  """
  if not line.startswith("#"):
    words = line.split()
    lst = list(words)
    lst = lst[:7]
    lst.reverse()
    for n,i in enumerate(lst):
      if i=='*':
        lst[n] = '0'
    showJobs(lst)


def main(argv):
  infile = open(str(sys.argv[1]))
  lines = infile.readlines()

  for line in lines:

    processlines(line)

  infile.close()

if __name__ == "__main__":
  main(sys.argv[1:])

