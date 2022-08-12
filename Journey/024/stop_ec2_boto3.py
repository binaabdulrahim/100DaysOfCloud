'''Scenario: Our DevOps engineering team often uses a development lab to test releases of our application. The Managers are complaining about the rising cost of our development lab and need to save money by stopping our (for this example) 3 ec2 instances after all engineers are clocked out.

**Create a Python script that you can run that will stop all instances.**'''

#since we dont have 3 ec2 instance right, lets first create 3 ec2 instance to test this
import boto3

ec2_res=boto3.resource('ec2')
ec2_res.create_instances(ImageId='ami-090fa75af13c156b4',
    InstanceType='t2.micro',
    MaxCount=4,
    MinCount=3)

#python script to stop all ec2 instance at end of the day
response = client.stop_instances(
    InstanceIds=[
        'string',
    ],
    Hibernate=True
)
#stop instances in dev environment only

#turn script into lambda function 