import re
import resource
from urllib import response
import boto3
#create s3 bucket using boto3

# aws_resources=boto3.resource('s3')
# bucket=aws_resources.Bucket('s3bucketusingboto33')

# response = bucket.create(
     ACL='private',
     CreateBucketConfiguration={
         'LocationConstraint':'us-east-2'
     },
 )
 print(response)

#list all buckets
s3 = boto3.client("s3")
 buckets_reponse = s3.list_buckets()
 for bucket in buckets_reponse["Buckets"]:
     print(bucket)

#list all objects in a bucket
 BUCKET_NAME = "s3bucketusingboto3"
 response = s3.list_objects_v2(Bucket=BUCKET_NAME)
for obj in response["Contents"]:
     print(obj)

#find the s3 bucket creation date using boto3

buckets_reponse = s3.list_buckets()
for bucket in buckets_reponse["Buckets"]:
    print(bucket)
    print(bucket["CreationDate"])