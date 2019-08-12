import requests

# input data as an array of dictonaries
data = [{'id': 1, 'name': 'iFunded', 'url': 'https://ifunded.de/en/'}, 
        {'id':2, 'name': 'Property Partner', 'url': 'https://www.propertypartner.co'},
        {'id':3, 'name': 'Property Moose', 'url': 'https://propertymoose.co.uk'},
        {'id':4, 'name': 'Homegrown', 'url': 'https://www.homegrown.co.uk'},
        {'id':5, 'name': 'Realty Mogul', 'url': 'https://www.realtymogul.com'}]

# API Key for screenshotmachine
key = ''


for i in range(5):

    payload = {'key': key, 'url': data[i].get('url'), 'dimension': '1920x1080', 'device': 'desktop'}

    r = requests.get('http://api.screenshotmachine.com/', params=payload)

    if r.status_code == 200:

        filename = str(data[i].get('id')) + '_' + data[i].get('name') + '.jpg'

        with open(filename, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=128):
                fd.write(chunk)
