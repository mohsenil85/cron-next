import time
import datetime
import conversions

class Job:
  """
  Class deffinition for Job.  Since each line in the file generally has the same forma
  we just scan each line and then split it into a list of words, and then each
  field is populated by indexing that list.  
  """
  def __init__(self, list):
    self.jobTitle = list[0]
    self.jobType = list[1]
    self.dayOfWeek = list[2]
    self.month = list[3]
    self.dayOfMonth = list[4]
    self.hour = list[5]
    self.minute = list[6]

  def processJobs(self, time):
    """
    Each field, gets converted into a number of seconds, which are added to to the
    time which the constructor was called.  Drawbacks to this are discussed in the
    README, essentially this approach is too brittle.  

    """
    try:
      jobTime = conversions.minToSec(int(self.minute)) + \
      conversions.hourToSec(int(self.hour)) + \
      conversions.dayToSec(int(self.dayOfMonth)) + \
      conversions.monthToSec(int(self.month)) + \
      time 

      # What an ugly line of code.  This is another example of a time where it would
      # have been easier and cleaner to just natively be using the datetime object
      # to store the jobs
      prettyTime =  datetime.datetime.fromtimestamp(jobTime).strftime('%Y-%m-%d %H:%M:%S')
      print "Job name:", self.jobTitle, "type:", self.jobType, "at time",  prettyTime
    except TypeError:
      print "Type error registered."
      pass
    except ValueError:
      #print "Value error registered."
      pass

