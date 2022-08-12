from http import client
from urllib import response
import boto3
client=boto3.client("ec2")

#create vpc
client.create_vpc(CidrBlock='10.0.0.0/16')

#delete vpc
response = client.delete_vpc(
    VpcId='vpc-0f6bfhslabfb345'
)