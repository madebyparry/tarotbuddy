#!/usr/bin/env python3
import colorama
import inquirer
import json
import os, sys, time, random

#
# TODO: Prettify
#       Make web ready functions
#       Split file contents
#       Define inverted cards
#       Better spreads
#       
# Cont: Path set
#       Set card vars
#       Intro
#       Initial selections
#       Triage selections
#       Functional script
#       Return to initial selections
#

# Path and data get
tbd = os.path.dirname(os.path.realpath(__file__))
f = open(tbd + '/data/reference.json')
data = json.load(f)
f.close()
f = open(tbd + '/data/dialog.json')
dialog = json.load(f)
f.close()


# Card variables
cards = data['tarot_cards']
rom_num = data['rom_num']
summaries = data['summaries']
descriptions = data['descriptions']

#dialog variables


def main():
    print('\n\t')
    theatricalPrint('\t' + getGreetingStr(), 0.05)
    print('\n')
    time.sleep(0.5)
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
        progressBar(i, 10)
    sys.stdout.write('''\n\t|___________________________________________| ''')
    sys.stdout.flush()


def progressBar(count_value, total, suffix=''):
    bar_length = 30
    filled_up_Length = int(round(bar_length* count_value / float(total)))
    percentage = round(100 * count_value/float(total))
    bar = '*' * filled_up_Length + '-' * (bar_length - filled_up_Length)
    if percentage < 100:
        sys.stdout.write('\t| | %s | %s%s %s | |\r' %(bar, percentage, '%', suffix))
        sys.stdout.flush()
    else:
        sys.stdout.write('\t| | % * : % * , DONE * # * . * % * , * | |')
        sys.stdout.flush()

# Aesthetic functions
def theatricalPrint(message, t = 0.025):
    c = 0
    for i in message:
        if c > 60 and i == " ":
            sys.stdout.write(i)
            sys.stdout.flush()
            c = 0
            print()
        else:
            time.sleep(t)
            sys.stdout.write(i)
            sys.stdout.flush()
            c = c + 1


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
    greeting = dialog['greetings'][random.randint(0,(len(dialog['greetings']) - 1))]
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
            ('Information','i'),
            ('Exit','d')
        ])]
    initial_choice = inquirer.prompt(initial_question)
    triageSelection(initial_choice['Initial_input'])

def triageSelection(user_in):
    if user_in == 'p':
        pullCard()
        main()
    elif user_in == 's':
        selectSpread()
    elif user_in == 'l':
        selectLookup()
        main()
    elif user_in == 'i':
        programInfo()
    elif user_in == 'd':
        print('Bye bye!')
    else: 
        print('bruh')

# Program functions
def selectSpread():
    thinking(1,5)
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
    for i in range(11):
        time.sleep(random.random())
        progressBar(i, 10)
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
    os.system('catimg -w 120 ' + tbd + '/data/img/' + str(r) + '.png')
    theatricalPrint(rom_num[r], 0.1)
    time.sleep(1)
    theatricalPrint(cards[r], 0.1)
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
    os.system('catimg -w 90 ' + tbd + '/data/img/' + str(x) + '.png')
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


# Program start
progressBarStart()
main()