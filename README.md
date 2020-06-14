# Dashboard

![alt text](https://github.com/A-Wheeto/Dashboard/blob/master/dashboard.JPG?raw=true)

## Scripts

- Dashboard.py - Main Dashboard script that draws the form and inserts text/images.
- xplane.py - Web scrapes data from threshold.net
- hddspace.py - Uses the module psutil to grab hard drive capacities
- news.py - Calls newsapi.org and grabs the latest BBC headlines
- piholeget.py - Calls my Raspberry Pi on home network and gets PiHole data (web scrapes Temp and Memory usage)
- steam.py - Web scrapes steampowered.com for the latest top selling games.
- weather2.py - Calls openweathermap API and gets 7 day weather for York, UK.

Run Dashboard.py for the main program, this imports the 6 other scripts which have been seperated for easy editing.

## Built With

* [tkinter](https://docs.python.org/3/library/tkinter.html) - GUI creation and drawing
* [PIL](https://pillow.readthedocs.io/en/stable/) - Python Imaging Library
* [PiHole](https://pypi.org/project/PiHole-api/) - Used to gather PiHole information
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Web scraping Steam, Pi Hole and Threshold
* [psutil](https://pypi.org/project/psutil/) - Gathers hard drive capacity information
