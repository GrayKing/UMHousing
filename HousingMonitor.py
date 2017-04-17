#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-12 22:05:02
# @Author  : Tom Hu (h1994st@gmail.com)
# @Link    : http://h1994st.com
# @Version : 1.0

import sys
import time
import getpass
from pprint import pprint

import requests
from lxml import html

import pushbullet
from pushbullet import Pushbullet

LOGIN_PAGE_URL = 'https://weblogin.umich.edu/'
LOGIN_POST_URL = 'https://weblogin.umich.edu/cosign-bin/cosign.cgi'
HOUSING_PAGE_URL = 'https://studentweb.housing.umich.edu'
APARTMENT_SELECTION_PAGE_URL = 'https://studentweb.housing.umich.edu/SelectRoom.asp?Function=6164'
SEARCH_ROOM_URL = 'https://studentweb.housing.umich.edu/SelectRoomResults.asp'

NO_RESULT_TEXT = 'There are no rooms available that match your search.'

# Please refer to related document on 'pushbullet.com'
PUSHBULLET_API_KEY = None  # Please set your own pushbullet access token
PUSHBULLET_DEVICE_NAME = None  # Please set your own device name

if PUSHBULLET_API_KEY is None:
    print >> sys.stderr, 'Please set your own pushbullet access token'
    sys.exit(1)

try:
    pb = Pushbullet(PUSHBULLET_API_KEY)
except pushbullet.errors.InvalidKeyError:
    print >> sys.stderr, 'Wrong api key!'
    sys.exit(1)

if PUSHBULLET_DEVICE_NAME is None:
    print >> sys.stderr, 'Please set your own device name'
    sys.exit(1)

try:
    device = pb.get_device(PUSHBULLET_DEVICE_NAME)
except pushbullet.errors.InvalidKeyError:
    print >> sys.stderr, 'Wrong device name!'
    device_names = [device.nickname for device in pb.devices]
    print >> sys.stderr, 'Please select from:', ','.join(device_names)
    sys.exit(1)

session_requests = requests.session()


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

    session_requests.get(APARTMENT_SELECTION_PAGE_URL)

    print 'Search'
    result = session_requests.post(
        SEARCH_ROOM_URL, data=payload)

    if result.status_code / 100 != 2:
        print 'Failed'
        return None

    if result.text.find(NO_RESULT_TEXT) != -1:
        # No result
        print 'No result'
        return None

    print 'Results!'
    return result


def login(username, password):
    payload = {
        'ref': '',
        'service': '',
        'required': '',
        'login': username,
        'password': password
    }

    # Get cookie
    print 'Get cookie'
    result = session_requests.get(LOGIN_PAGE_URL)
    if result.status_code / 100 != 2:
        print 'Failed'
        return False

    # Login
    print 'Login'
    result = session_requests.post(
        LOGIN_POST_URL, data=payload)

    if result.status_code / 100 != 2:
        print 'Failed'
        return False

    return True


def extract_info_from_result(result):
    tree = html.fromstring(result.text)
    elems = tree.cssselect('table.DataTable tr')[1:]

    departments = []
    for elem in elems:
        vals = elem.cssselect('td')
        vals[0] = vals[0].cssselect('a')[0]

        department = {
            'Name': vals[0].text,
            'link': vals[0].get('href'),
            'Area': vals[1].text,
            'Apartment Type': vals[2].text,
            'Contract Start Date': vals[3].text,
            'Square Footage': vals[4].text,
            'Environment': vals[5].text,
            'Air Conditioning': vals[6].text,
            'Furniture Type': vals[7].text,
            'Bedroom Dimensions': vals[8].text,
            'Available Space': vals[9].text
        }

        departments.append(department)

    return departments


def main():
    username = raw_input('Uniqname: ')
    while username.strip() == '':
        print >> sys.stderr, 'Uniqname cannot be empty.'
        username = raw_input('Uniqname: ')

    pwd = getpass.getpass()

    if login(username, pwd):
        while True:
            res = search()

            if res is not None:
                departments = extract_info_from_result(res)
                pprint(departments)

                simple_info = [(
                    '%s (Space: %s)' % (
                        department['Name'],
                        department['Available Space'])) for department in departments]

                device.push_note(
                    'NORTHWOOD!!!!!!!', '\n'.join(simple_info))

                print 'Sleeping 60 minutes...'
                time.sleep(60 * 60)
            else:
                print 'Sleeping 30 minutes...'
                time.sleep(30 * 60)


if __name__ == '__main__':
    main()
