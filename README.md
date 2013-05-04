cron-next
=========

reads the entries in a crontab file and then, for each job, determines the date/time the job will next run

How It Is Supposed To Work
--------

I'm pretty sure I would do it differently, given the chance to re-write it.  
Each line in the crontab file is converted to a Job object, and then each numerical
field in the Job is converted into seconds.  Every time an Job is instantiated, a call
is made to time.time() and stored in the variable `now`, and then the total amount of
seconds is added to `now`.  

Why It Doesn't
-----

### Conversions

### Job Class
