#!/usr/bin/python
# -*- coding: utf-8 -*-
# browser history noise
import random
import sys
try:
    import requests
except ImportError:
    raise ImportError("This script requires the module 'requests'. Try 'pip install requests' in your command line.")

noise = [
    'how to buy drugs online',
    'how to buy drugs via tor',
    'how to kill jews',
    'using tor to buy drugs',
    'how to hire an assassin',
    'how to murder fbi',
    'how to kill a law enforcement officer',
    'dark net assassin',
    'how to hire contract killer',
    'how to buy heroin online',
    'how to self print gun for murder',
    'how to make chemical bomb',
    'cp',
    'animal pornography',
    'how to cover up murder',
    'buy guns on tor',
    'best darknet market',
    'exchanging bitcoins for drugs',
    'exchanging bitcoins for murder',
    'how to kill a child',
    'how to beat a child to death',
    'how to buy m4a1 darknet',
    'how to load m4a1 for shooting people',
    'darknet child pornography',
    'darknet tor',
    'darknet market',
    'murdering a law enforcement officer',
    'how to kill an fbi agent',
    'how to steal weapons from fbi',
    'how to make a dirty bomb',
    'how to join nazis',
    'stormfront how to join',
    'using darknet for murder',
    'using darknet for drugs',
    'how to inject baby with heroin',
    'murder an nsa offical',
    'how to kill the president',
    'how to kill a government official',
    'how to kill hillary clinton',
    'how to bomb congress',
    'how to bomb a government building',
    'how to make napalm',
    'anarchist cookbook',
    'buy torture instruments online',
    'hire murder online',
    'hire murder tor',
    'how to hire contract killer tor',
    'how to make a bomb',
    'am i a psychopath',
    'how to become a terrorist',
    'am i being watched',
    'hydrogen bomb how',
    'lol nsa',
    'zoophilia forum',
    'am i a nazi',
    'why are jews bad',
    'i want to kill everyone is this normal',
    'pedo porn',
    'loli porn',
    'how do i doxx someone',
    'how do i hack the mainframe',
    'how to hack into the government',
    'how do i stage a coup',
    'buy guns where',
    'how to fire rifle',
    'shooting guns how',
    'how to create atom bomb',
    'staging a terrorist attack for dummies',
    'buy cocaine online',
    'buy heroin online',
    'buy illegal drugs online',
    'silk road 2.0',
    'silk road',
    'the dark web',
    'criminal stuff',
    'how to pick a lock',
    'how to dispose of a body',
    'uzi purchase online',
    'how to make a grenade',
    'buy shotgun with cash',
    'killing people bad?',
    'buy organs cheap deepweb',
    'where to sell organs for bitcoins',
    'sell newborns on tor',
    'how to buy a sex slave',
    '3 guys 1 hammer',
    'is it possible to kill a feminazi by making her think',
    'where download child porn',
    'free cheese pizza',
    'how to join podesta clinton child sex ring',
    'human trafficking 101',
    'is pizzagate real',
    'how to join isis',
    'where are extremist mosques in france',
    'i rape young girls on a weekly basis am i sick',
    'french nuclear physicists',
    'buy uranium online',
    'how to plug detonator on bomb',
    '2 phones 1 bomb',
    'white pride meetings 2018',
    'am i a pedophile',
    'where can i find daisy destruction',
    'peter scully bitcoin donation',
    'how to kill someone without being caught',
    'best way to spread airborne virus',
    'how to make chemical weapons',
    'buy aids darkweb',
    'is it possible to spread aids in town water system',
    'marathon bombers annual meeting 2018',
    'where is tamerlan tsarnaev buried',
    'is osama bin laden alive',
    'was osama bin laden a cia agent',
    'how to become a spy',
    'join special forces black ops',
    'mercenary training camps syria',
    'buy ghb tor',
    'how to lace fentanyl in xanax',
]
number_of_requests = 0

while True:
    # Select query
    query = random.choice(noise)

    # Clear screen
    print(chr(27) + "[2J")

    # Set up message
    number_of_requests += 1
    noun = 'requests' if number_of_requests is not 1 else 'request'

    # Display message
    print("👩‍💻 put-me-on-a-watchlist.py")
    print("~~~")
    print("We're gonna do some dubious Google searches for you. Sit tight.")
    print("Feel free to run this process in the background.\n")
    print(
        "Made %d %s. Press CTRL + C to stop" %
        (number_of_requests, noun)
    )
    print("\tSearched for \"%s\"" % query)

    # Make the request
    try:
        requests.get("http://www.google.com/?q=%s" % query)
    except (KeyboardInterrupt, SystemExit):
        print(
            "\n\t%d %s made in total. Bye!" %
            (number_of_requests, noun)
        )
        sys.exit()
