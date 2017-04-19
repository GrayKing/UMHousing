Housing Monitor
===

This is a python script for monitoring Northwood apartments. You should know that this script can only help you search apartments and push notification to the device immediately. It cannot automatically confirm the selection of the available apartment or accept the contract because I do not know the steps followed by a successful search.

Currently, I use [`Pushbullet`](https://www.pushbullet.com/) to push notifications to mobile devices (e.g., iPhone). An alternative notification solution is IFTTT [Maker Webhooks](https://ifttt.com/maker_webhooks). You can also replace this part of codes with other solutions (e.g., email, desktop notification, etc.).

### Getting started

_(All the commands can work well in both Ubuntu and macOS.)_

1. At first, you can use Git to clone this repository or click [here](https://github.com/h1994st/UMHousing/archive/master.zip) to directly download the script.

    ```bash
    $ git clone https://github.com/h1994st/UMHousing.git
    ```

2. Then, please enter the folder and set the configuration file according to the template.

    ```bash
    $ cd UMHousing
    $ cp conf.json.example conf.json
    ```

3. Before executing the following commands, please set pushbullet access token and necessary device name in `conf.json` at first.

    ```bash
    $ sudo pip install -r requirements.txt  # Install requirements
    $ python HousingMonitor.py  # Run
    ```

### Search parameters

The default parameters are hard coded in [`HousingMonitor.py`](https://github.com/h1994st/UMHousing/blob/master/HousingMonitor.py). In the future, they may be converted to command line parameters or a configuration file. Related codes start from [line 74](https://github.com/h1994st/UMHousing/blob/master/HousingMonitor.py#L74). There are comments which show the valid parameter values.

```python
...

def search():
    payload = {
        'fld24526': 49,  # Ready to process: {49(Yes)}
        'fld24527': '',  # Furnishings: {Furnished, Unfurnished}
        'fld24524': 'August 16',  # Contract start date: {July 1, July 16, August 1, August 16, September 1, September 16}
        'dateflddtArrival': '8/15/2017',  # Arrival date: %-m/%-d/%Y (e.g., 8/15/2017)
        'dateValueflddtArrival': '',
        'fldFunction': 6164,
        'btnSubmit': 'Search'
    }

    ...

...
```
