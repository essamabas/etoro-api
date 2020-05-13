
########### Python 3.6 #############
import requests
import json
import os
import logging


class broker():


    # Positions
    def get_positions(self):
        headers = {
            'mode': 'Demo',
        }

        response = requests.get('https://localhost:8088/etoro-api/positions')
        if response.status_code ==  requests.codes.ok:
            logging.info(response.text)
            #data_json = json.loads(data)
        else:
            logging.warning("status-code:= "+ str(response.status_code) + "\n response.text:= "+ response.text)         

    def open_position(self, trade_type, 
                         instrument_id, stock_symbol, 
                         amount , leverage=0, 
                         stop_loss_limit=0, take_profit=0):

        headers = {
            'accept': '*/*',
            'mode': 'Demo',
            'Content-Type': 'application/json',
        }

        data = '{"instrumentId": "'+ str(instrument_id) + '","name": "' + str(stock_symbol) + '","type": "' + trade_type + '","amount": ' + str(amount) + ',"leverage": '+ str(leverage) + ',"takeProfitRate": ' + str(take_profit) + ',"stopLossRate": '+ str(stop_loss_limit) + '}'
        response = requests.post('http://localhost:8088/etoro-api/positions/open', headers=headers, data=data)
        if response.status_code ==  requests.codes.ok:
            logging.info(response.text)
            #data_json = json.loads(data)
        else:
            logging.warning("status-code:= "+ str(response.status_code) + "\n response.text:= "+ response.text)  

    # WatchLists
    def get_watchlist(self):
        headers = {
            'cache-control': 'no-cache',
            'mode': 'Demo',
        }
        response = requests.get('http://localhost:8088/etoro-api/watchlist', headers=headers)
        if response.status_code ==  requests.codes.ok:
            logging.info(response.text)
            #data_json = json.loads(data)
        else:
            logging.warning("status-code:= "+ str(response.status_code) + "\n response.text:= "+ response.text)         


    def add_to_watchlist(self, stock_symbol):
        headers = {
            'Content-Type': 'application/json',
            'cache-control': 'no-cache',
        }
        data = '{\n \t"param": "' + stock_symbol + '"\n }'
        response = requests.put('http://localhost:8088/etoro-api/watchlist/byName', headers=headers, data=data)
        if response.status_code ==  requests.codes.ok:
            logging.info(response.text)
            #data_json = json.loads(data)
        else:
            logging.warning("status-code:= " + str(response.status_code) + "\n response.text:= "+ response.text)        

def main():

    mBroker = broker()
    
    #mBroker.get_watchlist()
    mBroker.get_positions()
    mBroker.open_position( trade_type = "BUY", 
                         instrument_id = 100000,
                         stock_symbol="btc",
                         amount= 100)

    
    mBroker.add_to_watchlist("Oil")
    
    pass

if __name__ == '__main__':
    main()