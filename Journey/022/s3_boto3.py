from fileinput import filename
import boto3

s3_resource=boto3.client("s3")

#upload file
s3_resource.upload_file(
    Filename="upload.png"
    Bucket="s3bucketusingboto3",
    Key="uploadtest.png"
)
#delete object
s3_resource.delete_object(Bucket='s3bucketusingboto3',
Key='uploadtest.png')