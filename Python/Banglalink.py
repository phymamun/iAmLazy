#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: Banglalink.py
# Created: Friday, 10th April 2020 10:12:40 pm
# Author: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Last Modified: Saturday, 11th April 2020 1:09:42 am
# Modified By: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Copyright (c) 2020 Slishee
###

"""
My intend to use this script as a cronjob
as Banlglalink gives out 25mb for free on
daily login to their ecare portal
through mobile app or using web portal.

I run this script daily on 11:00 AM

Crontab:
0 11 * * * python3 ~/Cronjobs/Banglalink.py
"""

import requests

# These values should be provided before running this script
mobile = ''  # User's Mobile Number (11 Digit)
password = ''  # User's Password

# The url to where Banglalink web page sends POST Requests
base_uri = 'https://eselfcare.banglalink.net/home/index'
# Setting a session to retrieve and pass csrfToken
rq = requests.Session()

def login(url, token, mobile, password):
    """
    Function to login to the user Portal

    Args:
        url: URL to fetch
        token: csrfToken to bypass xss protection
        mobile: User's mobile Number
        password: Password for the user account

    Returns:
        True: On Successfull Login
        False: If anything occurs else of 200 response
    """

    # The POST data to send over
    data = {
        '_method': 'POST',
        '_csrfToken': token,
        'mobile': mobile,
        'password': password
    }

    # Copied header
    # No guarantee to work al the time
    header = {
        "Host": "eselfcare.banglalink.net",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Length": "200",
        "DNT": "1",
        "Connection": "keep-alive",
        "Cookie": f"csrfToken={token}"
    }

    # The actual POST request
    res = rq.post(url, data=data, headers=header, allow_redirects=True)

    if res.status_code == 200:
        return True
    return False

def main(mobile, password):
    """
    Controlls the programs execution

    Args:
        mobile: User's mobile Number
        password: Password for the user account

    Returns:
        True: on Successfull Login
        False: on Failed Login
    """

    # Trying to make a fake request to get a seesion and csrfToken
    # to use it later
    html = rq.get(base_uri)
    token = rq.cookies.get_dict()['csrfToken']

    if login(base_uri, token, mobile, password):
        print('\n\n[+] Login Succeed!\n[+] Wait for the Megabytes to reach!\n\n')
        return True

    print('\n\n[-] Login Failed!\n\n')
    return False

if __name__ == '__main__':
    main(mobile, password)
