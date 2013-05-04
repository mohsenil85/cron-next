def minToSec(min):
  return 60*min

def hourToSec(hour):
  return 60*minToSec(hour)

def dayToSec(day):
  return 24*hourToSec(day)

def monthToSec(month):
  return 12*dayToSec(month)

def dayOfWeek(dow):
  return dayToSec(dow)
