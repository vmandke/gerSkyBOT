gerSkyBOT
=========

Gerrit Skype Bot

It takes updates from the gerrit and puts it on skype.
An easy way to track patches submitted for review and merged to master... 
This uses 'gerrit query' to query for recent merges and open patches. 



Run the setup.py to install the required Skype4py.

      $> python setup.py install
      
Add a crontab entry to run this script after every 10 mins, on working days Mon - Fri between 10:00 am - 8:00 pm

      $> chmod +x /path/gerritSkypeBot.py
  
      $> crontab -e
      add following:: */10 10-20 * * 1-5   DISPLAY=:0;export DISPLAY;/path/gerritSkypeBot.py

Please edit the config.json...
