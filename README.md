# automatic_online_class_scheduler
Automatic_online_class_scheduler is an application where it automatically opens the online platform where the class is going to be conducted at a specific time.

My college recently started online classes and they provided an excel sheet (time table) and they have mentioned time,date,subject,staff,link it was very confusing for me as to which link was to which class and stuff (just say I am lazy). 

So wanted to try selenium to automate this where it gets the current time and date, searches for those credentials in the 'sch.csv' and gets the link corresponding to that and opens respective links (currently we use Google Meet and Zoom) and ofcourse disables mic and camera by itself and waits for you to click the join button.

As of now I only created it to work on linux.

# Requirements

- Chrome driver - can get easily by googling, after downloading move the file to project directory
- selenium - pip3 install selenium
- pandas - pip3 install pandas
- numpy - pip3 install numpy

# Files

- script.py - just run it if you have already configured the data in sch.csv
- add_schedule.py - if you want to add any other new schedules or append to the previous schedule file.

# Improvements 

- wanted to automatically run the script at specific time using crontab linux which is easy but lazy but will do later.
- actually scrape data from my college whatsapp group so I need not need to configure it simply.

### Try it and also add your username / password for the google meet link in script.py login_account function.
