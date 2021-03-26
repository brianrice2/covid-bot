```
# min (0-59)
## hour (0-23)
### day of month (1-31)
#### month (1-12)
##### day of week (0-6, start on Sunday, or use names; 7 is also Sunday)

# run at 9am every day
# change these paths as needed
0 9 * * * /usr/local/anaconda3/bin/python ~/dev/covid-bot/main.py
```
