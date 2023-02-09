#!/usr/bin/python3
"""0. Gather data from an API
"""

from json import load
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
    user = make_request('users', ('id', user_id))
    tasks = make_request('todos', ('userId', user_id))
    tasks_completed = [task for task in tasks if task['completed']]
    print('Employee {} is done with tasks({}/{}):'.format(user[0]['name'],
                                                          len(tasks_completed),
                                                          len(tasks)))
    for task in tasks_completed:
        print('\t {}'.format(task['title']))


if __name__ == "__main__":
    main(argv[1])
