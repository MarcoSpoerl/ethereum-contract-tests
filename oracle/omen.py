import json
import sys
import time

from web3 import Web3, KeepAliveRPCProvider

web3 = Web3(KeepAliveRPCProvider(host='bootstrap', port='8545'))
oracle_abi = json.loads('[{"constant":false,"inputs":[],"name":"kill","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_something","type":"string"},{"name":"_callback","type":"function"}],"name":"query","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_requestId","type":"uint256"},{"name":"_response","type":"string"}],"name":"reply","outputs":[],"payable":false,"type":"function"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_requestId","type":"uint256"},{"indexed":false,"name":"_someParameter","type":"string"}],"name":"OracleRequest","type":"event"}]')
oracle_contract = web3.eth.contract(oracle_abi)

def new_block_callback(block_hash):
    sys.stdout.write('New block: {}\n'.format(block_hash))

def oracle_request_callback(event_log):
    sys.stdout.write('New oracle request: {}\n'.format(event_log))
    args = event_log['args']
    request_id = args['_requestId']
    request_param = args['_someParameter']
    block_number = event_log['blockNumber']
    response = 'responding to request id {} with parameter {} in block {}'.format(request_id, request_param, block_number)
    web3.personal.unlockAccount(web3.eth.coinbase, '')
    oracle_address = event_log['address']
    oracle = oracle_contract(oracle_address)
    oracle.transact({'from': web3.eth.coinbase}).reply(request_id, response)

new_block_filter = web3.eth.filter('latest')
new_block_filter.watch(new_block_callback)

oracle_request_filter = oracle_contract.on('OracleRequest')
oracle_request_filter.watch(oracle_request_callback)

while True:
    time.sleep(1)
    sys.stdout.write('.')
