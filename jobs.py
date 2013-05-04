import time
import datetime
import conversions

class Job:
  def __init__(self, list):
    self.jobTitle = list[0]
    self.jobType = list[1]
    self.dayOfWeek = list[2]
    self.month = list[3]
    self.dayOfMonth = list[4]
    self.hour = list[5]
    self.minute = list[6]

  def toString(self):
    print self.jobTitle
    print self.jobType
    print self.dayOfWeek
    print self.month
    print self.dayOfMonth
    print self.hour
    
  
  def processJobs(self, time):
    try:
      jobTime = conversions.minToSec(int(self.minute)) + \
      conversions.hourToSec(int(self.hour)) + \
      conversions.dayToSec(int(self.dayOfMonth)) + \
      conversions.monthToSec(int(self.month)) + \
      time 

      prettyTime =  datetime.datetime.fromtimestamp(jobTime).strftime('%Y-%m-%d %H:%M:%S')
      print "Job name:", self.jobTitle, "type:", self.jobType, "at time",  prettyTime
    except TypeError:
      pass
    except ValueError:
      pass

