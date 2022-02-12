#!/usr/bin/env python

# This file is part of krakenex.
# Licensed under the Simplified BSD license. See `examples/LICENSE.txt`.

import krakenex

k = krakenex.API()
k.load_key('kraken.txt')

balances=k.query_private('Balance')
#this must be updated to get any asset
USD=balances['result']['ZUSD']
BTC=balances['result']['XXBT']
ETH=balances['result']['XETH']
ETH2=balances['result']['ETH2']
ETH2S=balances['result']['ETH2.S']
DOT=balances['result']['DOT']
DOTS=balances['result']['DOT.S']
DOTTOTAL=str(float(DOT)+float(DOTS))
ETHTOTAL=str(float(ETH)+float(ETH2)+float(ETH2S))

KrakenDataWrite=open("KrakenData.txt","w")
KrakenDataWrite.write("BTC")
KrakenDataWrite.write("\n")
KrakenDataWrite.write(BTC)
KrakenDataWrite.write("\n")
KrakenDataWrite.write("ETH")
KrakenDataWrite.write("\n")
KrakenDataWrite.write(ETHTOTAL)
KrakenDataWrite.write("\n")
KrakenDataWrite.write("USD")
KrakenDataWrite.write("\n")
KrakenDataWrite.write(USD)
KrakenDataWrite.write("\n")
KrakenDataWrite.write("DOT")
KrakenDataWrite.write("\n")
KrakenDataWrite.write(DOTTOTAL)
KrakenDataWrite.write("\n")

