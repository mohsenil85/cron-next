import sys, datetime, re, time

#def replace_stars(tup):

def processlines(line):
  if not line.startswith("#"):
    line.replace("*", "0")
    words = line.split()
    l = list(words)
    job = l[-1:]
    print str(job)
    l = l[:7]
    l.reverse()

    print l
    #t = tuple(words)
    #print t
      
now = datetime.datetime.now()





def main(argv):
  infile = open(str(sys.argv[1]))
  #print "name: " , infile.name
  lines = infile.readlines()

  for line in lines:

    processlines(line)

  infile.close()

if __name__ == "__main__":
  main(sys.argv[1:])

