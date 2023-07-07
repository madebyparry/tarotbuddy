#!/usr/bin/env python3
import colorama
import inquirer
import os, sys, time, random
fromSh = True
import tarotbuddy
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


def main():
    global tbd
    tbd = os.path.dirname(os.path.realpath(__file__)) + '/'
    tarotbuddy.loadData(tbd)
    print('\n\t')
    theatricalPrint('\t' + tarotbuddy.getGreetingStr(), 0.05)
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


# Enacting selection
def initialSelection():
    initial_question=[inquirer.List(
        'Initial_input',
        message=tarotbuddy.getGreetingStr(),
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
        tarotbuddy.programInfo()
    elif user_in == 'd':
        print('Bye bye!')
    else: 
        print('bruh')

def selectSpread():
    tarotbuddy.resetDeck()
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
    hand_got = tarotbuddy.pullSpread(selected_spread['spread'])
    displaySpread(hand_got)


def displaySpread(hand):
    hand.append('-- RETURN --')
    while True:
        current_spread=[inquirer.List(
            'card',
            message='And here is your hand',
            choices=hand
            )]
        selection = inquirer.prompt(current_spread)
        selected_card = selection['card']
        if selected_card == '-- RETURN --':
            main()
            return False
        else:
            index = tarotbuddy.cards.index(selected_card)
            lookup_card = tarotbuddy.lookupCard(index)
            prettyPrintResults(lookup_card, index)

def selectLookup():
    which_card=[inquirer.List(
        'choice',
        message= 'What card would you like to know more on?',
        choices= tarotbuddy.cards
    )]
    selected_card = inquirer.prompt(which_card)
    index = tarotbuddy.cards.index(selected_card['choice'])
    lookup_card = tarotbuddy.lookupCard(index)
    prettyPrintResults(lookup_card, index)

def pullCard():
    cardLen = len(tarotbuddy.cards) - 1
    r = random.randint(1,cardLen)
    lookup_card = tarotbuddy.lookupCard(r)
    prettyPrintResults(lookup_card, r)

def prettyPrintResults(list, index):
    thinking(5, 10)
    os.system('catimg -w 90 ' + tbd + 'data/img/' + str(index) + '.png')
    theatricalPrint(list[0], 0.05)
    theatricalPrint(list[1], 0.05)
    theatricalPrint(list[2])
    theatricalPrint(list[3])


# Program start
progressBarStart()
main()