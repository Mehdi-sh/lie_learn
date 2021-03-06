import os
import numpy as np
import requests


def download(url):
    base = os.path.basename(url)
    path = os.path.join(os.path.dirname(__file__), base)
    if not os.path.isfile(path):
        open(path, 'wb').write(requests.get(url).content)
    return np.load(path, encoding='latin1', allow_pickle=True)
