import js
import sys
import tarotbuddy

# Element vars
right_body = js.document.getElementById('body-right')
left_body = js.document.getElementById('body-left')
right_info = js.document.getElementById('info-container')
user_select = js.document.getElementById('user-select')
list_wrapper = js.document.getElementById('list-wrapper')
select_container = js.document.getElementById('select-container')
card_num = js.document.getElementById('card-num')
card_name = js.document.getElementById('card-name')
card_img = js.document.getElementById('card-img')
card_sum = js.document.getElementById('card-sum')
card_desc = js.document.getElementById('card-desc')

spreads_available = {
    'Celtic Cross':10,
    'Horoscope Wheel':12,
    'Problem/Solution':2,
    'Past, Present, Future':3
}

def init():
    tarotbuddy.loadData()
    tarotbuddy.resetDeck()
init()

# Print Functions
def printLookup(list, index):
    card_num.innerHTML = list[0]
    card_name.innerHTML = list[1]
    card_sum.innerHTML = list[2]
    card_desc.innerHTML = list[3]
    card_img.src = 'data/img/' + str(index) + '.png'

# Operational Functions
def oneCard():
    your_card = tarotbuddy.pullCard(tarotbuddy.randCard())
    index = tarotbuddy.cards.index(your_card)
    single_card_result = tarotbuddy.lookupCard(index)
    printLookup(single_card_result, index)

def initSpreads():
    if list_wrapper.classList.contains('hidden'):
        list_wrapper.classList.remove('hidden')
    for i in spreads_available:
        opt = js.document.createElement('option')
        opt.value = spreads_available[i]
        opt.innerHTML = i
        user_select.appendChild(opt)
    
def getSpread():
    count = int(user_select.value)
    spread = tarotbuddy.pullSpread(count)
    counter = 0
    while len(list_wrapper.childNodes) > 2:
        if list_wrapper.hasChildNodes('p'):
            list_wrapper.removeChild(list_wrapper.childNodes[2])
    hr = js.document.createElement('hr')
    list_wrapper.appendChild(hr)
    for i in spread:
        counter += 1
        c = js.document.createElement('p')
        c.classList.add('spread-card')
        c.innerHTML = str(counter) + ') ' + i
        list_wrapper.appendChild(c)

def initLookup():
    if list_wrapper.classList.contains('hidden') == False:
        list_wrapper.classList.add('hidden')
    ul = js.document.createElement('ul')
    ul.classList.add('all-cards')
    right_body.appendChild(ul)
    counter = 0
    for i in tarotbuddy.cards:
        index = tarotbuddy.cards.index(i)
        li = js.document.createElement('li')
        li.value = index
        li.innerHTML = str(index) + ') ' + i
        ul.appendChild(li)


# BUTTONS
def drawButton():
    oneCard()

def speadsButton():
    initSpreads()

def lookupButton():
    initLookup()