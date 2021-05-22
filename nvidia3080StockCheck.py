# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 13:01:20 2020

@author: Harry Powell
"""
import requests
import time
from twilio.rest import Client

account_sid = 'ACa03f5a340823ccaa97082b443dd227c2'
auth_token = 'df13994658e7e8b2777ecd2ba59b4af8'
client = Client(account_sid, auth_token)


notifyMe = "NOTIFY ME"
AddCart = "Add to cart"
addCart = "add to cart"

preorder = "preorder"
preOrder = "preOrder"
Preorder = "Preorder"
PreOrder = "PreOrder"

pre_order = "pre order"
Pre_order = "Pre order"
Pre_Order = "Pre Order"

pre__order = "pre-order"
Pre__order = "Pre-order"
Pre__Order = "Pre-Order"


while True:
    page = requests.get("http://www.nvidia.com/en-gb/geforce/graphics-cards/30-series/rtx-3080/")
    #if notifyMe not in page.text:
    if notifyMe in page.text:
        break
    if (AddCart or addCart) in page.text:
        break
    if (preorder or preOrder or Preorder or PreOrder) in page.text:
        break
    if (pre_order or Pre_order or Pre_Order) in page.text:
        break
    if (pre__order or Pre__order or Pre__Order) in page.text:
        break
    print('Item isn\'t available for purchase yet')
    time.sleep(20)

print("Item is available for purchase")
message = client.messages \
    .create(
         body='TEST MESSAGE FROM HAROLD \nRTX 3080 in stock at http://www.nvidia.com/en-gb/geforce/graphics-cards/30-series/rtx-3080/ \nFrom your friend HaroldBOT2.0',
         from_='+447401238917',
         to='07580108305'
     )
message = client.messages \
    .create(
         body='TEST MESSAGE FROM HAROLD\nJIM Cheesepuff smells\nRTX 3080 in stock at http://www.nvidia.com/en-gb/geforce/graphics-cards/30-series/rtx-3080/ \nFrom your friend HaroldBOT2.0',
         from_='+447401238917',
         to='07725098298'
     )
     #07725098298
