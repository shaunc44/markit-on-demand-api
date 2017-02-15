#!/usr/bin/env python3

import requests


class Markit():

    def get_symbol():
        print(' ')
        company_name = input("What company do you want a symbol for? ")
        markit_api = 'http://dev.markitondemand.com/MODApis/Api/v2/Lookup/json/?input='
        symbol_urie = markit_api + company_name
        symbol_response = requests.get(symbol_urie)

        for _ in symbol_response.json():
            print(' ')
            print(_)
            # print(type(_))

#            print("Name: " + _['Name'])
#            print("Exchange: " + _['Exchange'])
#            print("Symbol: " + _['Symbol'])


    def get_quote():
        print('')
        ticker_symbol = input("What symbol do you want a quote for? ")
        markit_api = 'http://dev.markitondemand.com/MODApis/Api/v2/Quote/json/?symbol='
        quote_urie = markit_api + ticker_symbol
        quote_response = requests.get(quote_urie)

        counter = 0

        for _ in quote_response.json():
            if _ == 'LastPrice':
                cleprint(' ')
                print(_, quote_response.json()[_])
            # print(_, quote_response.json()['LastPrice'])
            # print(type(_))

#            print(' ')
#            print('This is indicative of a problem: ' + _)
            # print('Shaun\'s category: ' + _)
            # print(_['Name'])
            # print(_[0])
            # print(_[0:3])
            # print('hello world')

#            counter += 1

#            print('You\'ve already asked me for ' + ticker_symbol + " " + str(counter) + ' times!')

# Your code goes here. May the force be with us!