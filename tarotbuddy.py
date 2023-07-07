#!/usr/bin/env python3
# import colorama
import json
import random

# Path and data get
def loadData(tbd=''):
    global cards
    global rom_num
    global summaries
    global descriptions
    global dialog
    f = open(tbd + 'data/reference.json')
    card_data = json.load(f)
    f.close()
    f = open(tbd + 'data/dialog.json')
    dialog = json.load(f)
    f.close()
    
    # Card variables
    cards = card_data['tarot_cards']
    rom_num = card_data['rom_num']
    summaries = card_data['summaries']
    descriptions = card_data['descriptions']

def resetDeck():
    global card_deck
    global pulled_cards
    card_deck = cards
    pulled_cards = []
    card_deck = card_deck + cards


# Greetings getter
def getGreetingStr():
    greeting = dialog['greetings'][random.randint(0,(len(dialog['greetings']) - 1))]
    return greeting

# Program functions
def getHand(x):
    hand = {'name':[],'index':[]}
    cardLen = len(cards) - 1
    i = 0
    while i < x:
        r = random.randint(1,cardLen)
        hand['name'].append(cards[r])
        hand['index'].append(r)
        i = i + 1
    hand['name'].append('-- RETURN --')
    hand['index'].append(99)
    return hand

def lookupCard(x):
    lookupResults = [
        rom_num[x],
        cards[x],
        descriptions[x],
        summaries[x]
    ]
    return lookupResults

def programInfo():
    print('\n')
    print('Thanks for using Tarotbuddy!')
    print('This project is totally free and open source. A little project made by my wife and I')
    print('Be sure to check out the web version hosted at https://madebyparry.ddns.net/tarotbuddy')
    print('\n\t With love,')
    print('\n\t - MBP')

def randCard():
    r = random.randint(0, (len(card_deck) - 1))
    return r

def pullCard(x):
    pulled = card_deck[x]
    card_deck.pop(x)
    pulled_cards.append(pulled)
    return pulled

def pullSpread(count):
    i = 0
    spread = []
    while i < count:
        r = randCard()
        spread.append(pullCard(r))
        i += 1
    return spread
    