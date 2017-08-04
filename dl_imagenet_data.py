# Download Imagenet images

import argparse
import multiprocessing
import os
import sys
import urllib
import urllib2
import urlparse

def download_imagenet(urls_filepath, out_path):

    def retrieve_img_and_process(url_and_fp):
        url, fp = url_and_fp[0], url_and_fp[1]
        # print url, fp
        try:
            urllib.urlretrieve(url, fp)
        except Exception as e:
            print e

    urls = open(urls_filepath, 'rb').readlines()
    urls = [url.strip('\n') for url in urls]
    out_fps = [os.path.join(out_path, urlparse.urlparse(url).path.split('/')[-1]) for url in urls]

    from multiprocessing.dummy import Pool as ThreadPool
    pool = ThreadPool(4)
    urls_and_fps = zip(urls, out_fps)
    # print urls_and_fps
    for i in range(0, len(urls), 10):
        print i
        results = pool.map(retrieve_img_and_process, urls_and_fps[i:i+10])

if __name__ == '__main__':
    download_imagenet('data/imagenet_urls/crab.txt', 'data/imgs/imagenet/crab/')