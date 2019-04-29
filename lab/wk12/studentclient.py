import ssl, socket, pprint
import requests
import time
import json
from requests.auth import HTTPBasicAuth

server = "localhost:"
port = 8080

CREDS = {
    'username': 'guest',
    'password': 'password'
}


class Client:
    def __init__(self):
        self.httpGET = 'http://' + server + str(port) + '/messages'
        self.httpPOST = 'http://' + server + str(port) + '/message'
        self.httpsGET = 'https://' + server + str(port) + '/messages'
        self.httpsPOST = 'https://' + server + str(port) + '/message'

    def GetAllMessages(self, secure=False):
        if secure:
            print('trying https with creds:', CREDS['username'], CREDS['password'])
            return requests.get(url=self.httpsGET,
                                auth=HTTPBasicAuth(CREDS['username'], CREDS['password']),
                                verify='server.crt')
        else:
            print('trying https with creds:', CREDS['username'], CREDS['password'])
            return requests.get(url=self.httpGET,
                                auth=HTTPBasicAuth(CREDS['username'], CREDS['password']),
                                verify='server.crt')

    def SendAMessage(self, msg, secure=False):
        if secure:
            print('sending {} as {}\n', msg['message'], msg['sender'])
            message = json.dumps({'message': msg['message']})
            headers = {'content-type': 'application/json'}
            return requests.post(url=self.httpsPOST + msg['sender'],
                                 auth=HTTPBasicAuth(CREDS['username'], CREDS['password']),
                                 verify='server.crt',
                                 data=message,
                                 headers=headers)
        else:
            print('sending {} as {}\n', msg['message'], msg['sender'])
            message = json.dumps({'message': msg['message']})
            headers = {'content-type': 'application/json'}
            return requests.post(url=self.httpPOST + msg['sender'],
                                 auth=HTTPBasicAuth(CREDS['username'], CREDS['password']),
                                 verify='server.crt',
                                 data=message,
                                 headers=headers)


if __name__ == '__main__':
    c = Client()
    res = c.SendAMessage({'sender': 'Clemence', 'message': 'Simple Test'})
    print(res.status_code)
    res = c.GetAllMessages()
    print(res.content)
