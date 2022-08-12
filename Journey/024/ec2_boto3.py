import boto3

ec2_res=boto3.resource("ec2")

#launch ec2
ec2_res.create_instances(ImageId='ami-07c8bc5clce4598c',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1)

#get all ec2 instance id
x=ec2_res.describe_instances()
data=x["Reservations"][0]
data_instance=data["Instances"]
for i in range (len(data_instance)):
    print(f"instance id is {data_instance[i]['InstanceId']}")

#create multiple ec2s
ec2_res.create_instances(ImageId='ami-07c8bc5clce4598c',
    InstanceType='t2.micro',
    MaxCount=4,
    MinCount=3)

#terminate multiple ec2s
x=ec2_res.describe_instances()
data=x["Reservations"]
li=[ ]
for instances in data:
    instance=instances["Instances"]
    for ids in instance:
        instance_id=ids["InstanceId"]
        li.append(instance_id)

