import bs

def bsGetConfig():
    return {
        'sessionType': 'ffa',
        'playlistCode': '9UE0NK9Q',
        'serverName': 'GitHub+Ngrok Server',
        'port': 43210,
        'maxPlayers': 8,
        'announce': True,
        'partyIsPublic': True,
        'accountID': __import__('os').environ.get('BS_ACCOUNT_ID', 'pb-IF4cUHE9Eg==')
    }
