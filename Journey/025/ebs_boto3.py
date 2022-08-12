from telnetlib import ENCRYPT
import boto3

ec2_client=boto3.client("ec2")

#create ebs volume snapshot
ec2_client.create_volume(AvailabilityZone='us-east-2c',
    Encrypted=True,
    Size=12,
    SnapshotId='snap-09123bebe89ef',
    VolumeType='gp2')

#delete ebs volume snapshot
ec2_client.delete_snapshot(SnapshotId='snap-0937bebe9efse')

#describe ebs volume snapshot
ec2_client.describe_snapshots(SnapshotIds=['snap-0937bebe9efse'])