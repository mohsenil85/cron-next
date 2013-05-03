import sys, getopt

def main(argv):
  infile = open(str(sys.argv[1]))
  print "name: " , infile.name

  infile.close()

if __name__ == "__main__":
     main(sys.argv[1:])
