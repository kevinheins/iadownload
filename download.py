#!/usr/bin/env python

import requests
import argparse
from BeautifulSoup import BeautifulSoup
from internetarchive import download
import urllib3
urllib3.disable_warnings()

from internetarchive import get_item
config = dict(general=dict(secure=False))
item = get_item('<identifier>', config=config)

parser = argparse.ArgumentParser(description='Download a collection from internetarchive...')
parser.add_argument('collectionname', metavar='collection-name', action='store', help='The collection name from internetarchive')
#parser.add_argument('link-filter', metavar='N', nargs='+', help='Filter out the links returned')
args = parser.parse_args()
url = "http://archive.org/download/" + args.collectionname
response = requests.get(url)
# parse html
page = BeautifulSoup(response.content)
#https://archive.org/download/RedumpSonyPS2NTSCUPart2/MLB%20SlugFest%20-%20Loaded%20%28USA%29.7z

def download_file(url,targetfile):
    local_filename = targetfile
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True, verify=False)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    return local_filename

# for div in page.findAll('div', {'class': 'container container-ia'}):
#     a = div.findAll('a', href=True)
#     for link in a:
#         print url + "/" + link['href']
#     print url + "/" + a[20]['href']
# download_file(url + "/" + a[20]['href'], "a.7z")

download(args.collectionname, verbose=True)
