cron-next
=========

reads the entries in a crontab file and then, for each job, determines the date/time the job will next run

How It Is Supposed To Work
--------

I'm pretty sure I would do it differently, given the chance to re-write it.  
Each line in the crontab file is converted to a `Job` object, and then each numerical
field in the `Job` is converted into seconds.  Every time an Job is instantiated, a call
is made to `time.time()` and stored in the variable `now`, and then the total amount of
seconds is added to `now`.  

Why It Doesn't
-----

### Conversions
One way this approach fails is because it needs to know what the current day is in order 
to calculate how many days to offset for the weekly cronjobs.  For example, if 
something needs to run every other day, my script can not know whether the cron job
needs to be run in one day or in two days.  

### Job Class
If I could do this over again, I would make the Job class inherit from `datetime`,
and just have an extra field to store the actual job description.  I think the main
failure of this script is the failure to utilize the datetime class, hence all the
awkwardness converting everything into seconds, and then converting back.  Also
it makes it harder to to use this script in conjunctin with anthing else because it
doesn't return a new a new datetime object, it just prints (innacurate) stuff to 
the screen.

Also, the method of calling the constructor on a list is kind of flawed, because 
some of the information that is separated by spaces needs to be grouped together. 
calling words.split() was a bit too simplistic.

### Regex Flailure
I'll be the first to admit that my unfamiliarity with regexes.  I tried forever to
get it to read a string like `*\1`.  I'm not sure if the backslash escaped the 1, or
what exactly happened.  This is the sort of situation where the online help wasn't
very helpful, and it would just be so much easier to just ask someone.  Given more 
time, I am confident I could have at least solved this.


Considerations
---

I don't feel very good about this code.  Given the chance I would re-write it from
top to bottom.  Problems that need to be solved are:
    
    + Better regex/parsing of the files
    + Return an object instead of just printing stuff to screen
    + Calling an object with a list as a parameter is too brittle
