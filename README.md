cron-next
=========

reads the entries in a crontab file and then, for each job, determines the date/time the job will next run

### Usage

`python cron-next.py inputfile`

### Sample output:

    #MAILTO="test@parthenonsoftware.com"

    # minute, hour, dom, month, dow

    # minutely
    */1 *   *     * * php /app/site/cron/job1.php
    */1 15-23,0-5    *     * * php /app/site/cron/job2.php
    */2 *   *     * * php /app/site/cron/job3.php
    */5 *   *     * * php /app/site/cron/job4.php
    
    # hourly
    */10 *   *     * * php /app/site/cron/job5.php
    0    */2 *     * * php /app/site/cron/job6.php
    10   *   *     * * php /app/site/cron/job7.php
    
    # daily
    10  0   *     * * php /app/site/cron/job8.php
    25  0   *     * * php /app/site/cron/job9.php
    30  0   *     * * php /app/site/cron/job10.php
    45  10  */1   * * php /app/site/cron/job11.php
    1   20  *     * * php /app/site/cron/job12.php
    #15  18  *     * * php /app/site/cron/job13.php
    
    # weekly/monthly
    0   0   11,25 * * php /app/site/cron/job14.php
    
    # daily emails
    40 23 *        * *   php /app/site/cron/job15.php
    20 0 *        * *   php /app/site/cron/job16.php
    15 2 *        * 1-6   php -d "memory_limit=600M" /app/site/cron/job17.php
    50 2 1-6,8-31 * *   php /app/site/cron/job18.php
    0  3 *        * *   php /app/site/cron/job19.php
    
    # weekly emails
    48 0 *        * 2   php /app/site/cron/job20.php
    50 1 1-6,8-31 * 7   php /app/site/cron/job21.php
    
    # monthly emails
    0  0 2        * *   php /app/site/cron/job22.php
    

### Sample output:

    Job name: /app/site/cron/job7.php type: php at time 2013-05-03 22:28:52
    Job name: /app/site/cron/job8.php type: php at time 2013-05-03 22:28:52
    Job name: /app/site/cron/job9.php type: php at time 2013-05-03 22:43:52
    Job name: /app/site/cron/job10.php type: php at time 2013-05-03 22:48:52
    Job name: /app/site/cron/job12.php type: php at time 2013-05-04 18:19:52
    Job name: /app/site/cron/job15.php type: php at time 2013-05-04 21:58:52
    Job name: /app/site/cron/job16.php type: php at time 2013-05-03 22:38:52
    Job name: -d type: php at time 2013-05-04 00:33:52
    Job name: /app/site/cron/job19.php type: php at time 2013-05-04 01:18:52
    Job name: /app/site/cron/job20.php type: php at time 2013-05-03 23:06:52
    Job name: /app/site/cron/job22.php type: php at time 2013-05-05 22:18:52

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
