#!/usr/bin/python3
"""Export to JSON
"""

from json import dump
import requests
from sys import argv


def make_request(resource, param=None):
    """Retrieve user from API
    """
    url = 'https://jsonplaceholder.typicode.com/'
    url += resource
    if param:
        url += ('?' + param[0] + '=' + param[1])

    # make request
    r = requests.get(url)

    # extract json response
    r = r.json()
    return r


def main(user_id):
    user = make_request('users', ('id', user_id))[0]
    tasks = make_request('todos', ('userId', user_id))

    # format before exporting
    user_id = user['id']
    export = {user_id: []}
    for task in tasks:
        export[user_id].append({'task': task['title'],
                                'completed': task['completed'],
                                'username': user['username']})

    filename = str(user_id) + '.json'
    with open(filename, mode='w') as f:
        dump(export, f)


if __name__ == "__main__":
    main(argv[1])
