# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 13:01:20 2020

@author: Harry Powell
"""
import requests
import time
from twilio.rest import Client

from datetime import datetime

account_sid = 'replace_with_account_sid'
auth_token = 'replace_with_account_auth'
client = Client(account_sid, auth_token)

counter = 0
msgCount = 0

jimMsgCount = 0

loaded = 'NVIDIA GEFORCE RTX 3080 - GB'

productOutOfStock = 'PRODUCT_INVENTORY_OUT_OF_STOCK'
statusIsEstimatedFalse = '"statusIsEstimated": "false"'

requestedQuantityAvailableFalse = '"requestedQuantityAvailable": "false"'
requestedQuantityEstimatedFalse = '"availableQuantityIsEstimated": "false"'

while True:
    now = datetime.now()
    dt_string = now.strftime("[%d/%m/%Y-%H:%M:%S]")
    page = requests.get("https://google.com")
    time.sleep(1)
    try:
        page = requests.get("https://api-prod.nvidia.com/direct-sales-shop/DR/products/en_gb/GBP/5438792800", timeout=2)
        #page = requests.get("https://raw.githubusercontent.com/hydiar/RTX-3080-API-Stock-Check/main/5438792800.json", timeout =2)        #test
        time.sleep(1)
        if loaded in page.text:
            if productOutOfStock not in page.text:
                print(dt_string + " Nvidia RTX 3080 PRODUCT_INVENTORY_IN_STOCK")
                break
            counter += 1
            print(dt_string + ' Connected: Nvidia RTX 3080 isn\'t available for purchase yet, connection attempt: ' + str(counter))
            time.sleep(1)
        else:
            counter += 1
            print(dt_string + ' Bad Gateway, Connection attempt: ' + str(counter))
            time.sleep(1)
    except:
        counter += 1
        print(dt_string + ' Error connecting to page, connection attempt: ' + str(counter))
        time.sleep(1)

call = client.calls.create(
                        twiml='<Response><Say>Nvidia thirty eighty in stock</Say></Response>',
                        to='replace_with_your_phonenumber',
                        from_='replace_with_from_phonenumber'
                    )

while msgCount < 4:
    print("Nvidia RTX 3080 is available for purchase! - Sending SMS Notification")
    message = client.messages \
        .create(
             body='The RTX 3080 is in stock at https://www.nvidia.com/en-gb/shop/geforce/gpu/?page=1&limit=9&locale=en-gb&category=GPU&manufacturer=NVIDIA&gpu=RTX%203080 \nFrom your friend HaroldBOT2.0',
             from_='replace_with_from_phonenumber',
             to='replace_with_your_phonenumber'
         )
    msgCount += 1
    time.sleep(5)
