# COVID Bot

Sadly, [The COVID Tracking Project](https://twitter.com/covid19tracking?lang=en) has stopped their daily updates. This simple cron job delivers daily case and death counts to your command line `mail` account. Edit your cron jobs by typing `crontab -e` and copy the code from `cronjob.md` to schedule the recurring jobs (9am daily).

Note that cron jobs don't execute if your system is asleep, for example. This could/will be updated to `launchd`, which get rescheduled if your computer isn't powered off.
