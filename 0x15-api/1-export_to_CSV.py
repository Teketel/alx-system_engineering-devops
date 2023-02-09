#!/usr/bin/python3
"""Export to CSV
"""

import csv
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

    csv_filename = user_id + '.csv'
    with open(csv_filename, mode='w') as f:
        writer = csv.writer(f,
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([user['id'],
                            user['username'],
                            task['completed'],
                            task['title']])


if __name__ == "__main__":

    main(argv[1])
