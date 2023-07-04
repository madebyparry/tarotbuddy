#!/usr/bin/env python3
import colorama
import inquirer
import json
import os, sys, time, random

# Path and data get
tbd = os.path.dirname(os.path.realpath(__file__))
f = open(tbd + '/data/reference.json')
data = json.load(f)
f.close()

# Card variables
cards = data['tarot_cards']
rom_num = data['rom_num']
summaries = data['summaries']
descriptions = data['descriptions']


def main():
    progressBarStart()
    print('\n\t')
    theatricalPrint(getGreetingStr(), 0.1)
    print('\n')
    initialSelection()

# Intro progress bar
def progressBarStart():
    sys.stdout.write('''\t_____________________________________________
\t|  _______________________________________  |
\t| | % * ' % * , * ^ % * % # * . * % * , * | |
\t| | * % # * Welcome to TarotBuddy * # % * | |
\t| | % * ' % * , * ^ % * % # * . * % * , * | |
''')
    sys.stdout.flush()
    for i in range(11):
        time.sleep(random.random())
        progressBar(i,10)

def progressBar(count_value, total, suffix=''):
    bar_length = 30
    filled_up_Length = int(round(bar_length* count_value / float(total)))
    percentage = round(100 * count_value/float(total))
    bar = '*' * filled_up_Length + '-' * (bar_length - filled_up_Length)
    if percentage < 100:
        sys.stdout.write('\t| | %s | %s%s %s | |\r' %(bar, percentage, '%', suffix))
        sys.stdout.flush()
    else:
        sys.stdout.write('\t| | ------------------------------------- |')
        sys.stdout.write('''\n\t|___________________________________________| ''')
        sys.stdout.flush()

# Aesthetic functions
def theatricalPrint(message, t = 0.025):
    for i in message:
        time.sleep(t)
        sys.stdout.write(i)
        sys.stdout.flush()
    print('\n')

def thinking(a, b):
    r = random.randint(a, b)
    i = 0
    while i < r:
        time.sleep(random.random())
        sys.stdout.write(".")
        sys.stdout.flush()
        i = i + 1
    print('\n')

# Greetings getter
def getGreetingStr():
    greeting = data['greetings'][random.randint(0,(len(data['greetings']) - 1))]
    return greeting

# Enacting selection
def initialSelection():
    initial_question=[inquirer.List(
        'Initial_input',
        message=getGreetingStr(),
        choices=[
            ('Pull a card','p'),
            ('Spreads','s'),
            ('Card lookup','l'),
            ('Information','i')
        ])]
    initial_choice = inquirer.prompt(initial_question)
    triageSelection(initial_choice['Initial_input'])

def triageSelection(user_in):
    if user_in == 'p':
        pullCard()
    elif user_in == 's':
        selectSpread()
    elif user_in == 'l':
        selectLookup()
    elif user_in == 'i':
        programInfo()
    else: 
        print('bruh')

# Program functions
def selectSpread():
    which_spread=[inquirer.List(
        'spread',
        message='What fancies you?',
        choices=[
            ('Celtic Cross',10),
            ('Horoscope Wheel',12),
            ('Problem/Solution',2),
            ('Past, Present, Future',3)
        ])]
    selected_spread = inquirer.prompt(which_spread)
    displaySpread(getHand(selected_spread['spread']))

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

def displaySpread(hand):
    while True:
        current_spread=[inquirer.List(
            'card',
            message='And here is your hand',
            choices=hand['name']
            )]
        selection = inquirer.prompt(current_spread)
        selected_card = selection['card']
        if selected_card == '-- RETURN --':
            main()
            return False
        else:
            index = cards.index(selected_card)
            print('\n')
            lookupCard(index)


def pullCard():
    cardLen = len(cards) - 1
    r = random.randint(1,cardLen)
    thinking(5, 10)
    os.system('catimg -w 100 ' + tbd + '/data/img/' + str(r) + '.png')
    theatricalPrint(rom_num[r], 0.2)
    time.sleep(1)
    theatricalPrint(cards[r], 0.2)
    thinking(3,5)
    theatricalPrint(descriptions[r])
    thinking(3,5)
    theatricalPrint(summaries[r])

def selectLookup():
    which_card=[inquirer.List(
        'choice',
        message= 'What card would you like to know more on?',
        choices= cards
    )]
    selected_card = inquirer.prompt(which_card)
    index = cards.index(selected_card['choice'])
    lookupCard(index)


def lookupCard(x):
    thinking(2, 5)
    theatricalPrint(rom_num[x], 0.05)
    theatricalPrint(cards[x], 0.05)
    theatricalPrint(descriptions[x])
    theatricalPrint(summaries[x])

def programInfo():
    print('\n')
    print('Thanks for using Tarotbuddy!')
    print('This project is totally free and open source. A little project made by my wife and I')
    print('Be sure to check out the web version hosted at https://madebyparry.ddns.net/tarotbuddy')
    print('\n\t With love,')
    print('\n\t - MBP')
main()