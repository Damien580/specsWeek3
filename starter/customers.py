customers = {
    'mel': {'username': 'mel', 'password': 'password', 'name': 'Mel Wilson'},
    'squash': {'username': 'squash', 'password': '1234', 'name': 'Sara Squash'},
    'bunsen': {'username': 'bunsen', 'password': 'muppet', 'name': 'Bunsen Honeydew'},
    'hoon': {'username': 'hoon', 'password': 'blindmelon', 'name': 'Shannon Hoon'},
    'laserfalcon': {'username': "laserfalcon", 'password': 'bird', 'name': 'Damien Redd'}
}

def get_by_username(username):
    return customers.get(username)