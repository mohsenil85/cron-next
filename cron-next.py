import sys, time
import jobs

def showJobs(job):
  now = int(time.time())
  try:
    j = jobs.Job(job)
    j.processJobs(now)
  except IndexError:
    pass

def processlines(line):
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

