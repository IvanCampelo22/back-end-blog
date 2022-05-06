
import logging
import sys
import threading
from xmlrpc.client import SYSTEM_ERROR
import boto3
from botocore.exceptions import ClientError
import os

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)
    
#data = open("media/tileburnedin.jpg", "rb")
#s3.Bucket("atmhomerecifeblog").put_object(Key="tileburnedin.jpg", Body=data)


def upload_file(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = os.path.basename('media')
        
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


s3 = boto3.client('s3')
#with open("media/tileburnedin.jpg", "rb") as f:
#   s3.upload_fileobj(f, "atmhomerecifeblog", "tileburnedin.jpg")

#s3.upload_file(
    #'media/tileburnedin.jpg', 'atmhomerecifeblog', 'tileburnedin.jpg',
    #ExtraArgs={'ACL':'public-read'}
#)


#class Progresspercentage(object):
    
    #def __init__(self,filename):
        #self._filename = filename
        #self._size = float(os.path.getsize(filename))
        #self._seen_so_far = 0
        #self._lock = threading.Lock()
    
    #def __call__(self, bytes_amount):
        #with self._lock:
            #self._seen_so_far += bytes_amount
            #percentage = (self._seen_so_far / self._size) * 100
            #sys.stdout.write(
                #"\r%s %s / %s (% 2f%%)" %(
                    #self._filename, self._seen_so_far, self._size,
                    #percentage))
                
            #sys.stdout.flush()


#s3.upload_file(
    #'media/tileburnedin.jpg', 'atmhomerecifeblog', 'tileburnedin.jpg',
    #Callback=Progresspercentage('media/tileburnedin.jpg')
#)