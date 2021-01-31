import boto3
from botocore.client import Config
import mimetypes
import os

file = 'video.mp4'
extension = os.path.splitext(file)[1]
obj_key = "Video-Test"

ACCESS_KEY_ID = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx'
ACCESS_SECRET_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx'
BUCKET_NAME = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

data = open(file, 'rb')

s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)
s3.Bucket(BUCKET_NAME).put_object(Key=obj_key, Body=data, ContentType=mimetypes.MimeTypes().guess_type(file)[0])

print("Done")
