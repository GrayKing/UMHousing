Housing Monitor
===

This is a python script for monitoring Northwood apartments. Currently, I use [`Pushbullet`](https://www.pushbullet.com/) to push notifications to mobile devices (e.g., iPhone). An alternative notification solution is IFTTT [Maker Webhooks](https://ifttt.com/maker_webhooks). You can also replace this part of codes with other solutions (e.g., email, desktop notification, etc.).

### Getting started

Before executing the following commands, please open `HousingMonitor.py` and set pushbullet access token and necessary device name.

```bash
$ git clone https://github.com/h1994st/UMHousing.git
$ cd UMHousing
$ sudo pip install -r requirements.txt  # Install requirements
$ python HousingMonitor.py  # Run
```
