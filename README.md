Housing Monitor
===

This is a Python script for monitoring Northwood apartments. You should know that this script can only help you search apartments and push notification to the device immediately. It cannot automatically confirm the selection of the available apartment or accept the contract because I do not know the steps after a successful search.

Currently, this script uses [`Pushbullet`](https://www.pushbullet.com/) to push notifications to mobile devices (e.g., iPhone). An alternative notification solution is IFTTT [Maker Webhooks](https://ifttt.com/maker_webhooks). You can also replace this part of codes with other solutions (e.g., email, desktop notification, etc.).

Since the probability of a successful search is very low, I cannot comprehensively test this script. Although this script can send the correct notification in time and did help me get an apartment contract, please ___DO NOT___ completely rely on this script, unless you can improve this script and confirm its effectiveness. If any errors occur while using this script, please feel free to contact me. You can either choose to submit an [issue](https://github.com/h1994st/UMHousing/issues) on Github or create a [pull request](https://github.com/h1994st/UMHousing/pulls).

## Getting started

_(All the commands can work well in both Ubuntu and macOS.)_

1. At first, you can use Git to clone this repository or click [here](https://github.com/h1994st/UMHousing/archive/master.zip) to directly download the script.

    ```bash
    $ git clone https://github.com/h1994st/UMHousing.git
    ```

2. Then, please enter the folder and set the configuration file according to the template, if you need Pushbullet ___notification___.

    ```bash
    $ cd UMHousing
    $ cp conf.json.example conf.json  # Ignore this command, if you do not need notification
    ```

    To set Pushbullet ___access token___ and necessary ___device name___ in `conf.json`, please refer to the [document](https://docs.pushbullet.com/#api-quick-start) of Pushbullet.

3. Install dependencies.

    ```bash
    $ sudo pip install -r requirements.txt  # Install requirements
    ```

3. Run the script.

    ```bash
    $ python HousingMonitor.py  # Run
    ```

## Search parameters

The default parameters are hard coded in [`HousingMonitor.py`](https://github.com/h1994st/UMHousing/blob/master/HousingMonitor.py). In the future, they may be converted to command line parameters or a configuration file. Related codes start from [line 136](https://github.com/h1994st/UMHousing/blob/master/HousingMonitor.py#L136) of `HousingMonitor.py`. There are comments which show the valid parameter values.

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
