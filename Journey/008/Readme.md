![Pink Fun Cloud Mental Health Therapy Games Logo (1)](https://user-images.githubusercontent.com/41940176/147340937-89bd90d7-5096-40fe-943b-7bdc8551930a.gif)

# Create an S3 Bucket and store an object in it

## Introduction

* Each bucket's name has to be unique globally, across every single bucket in the world.
* Try to get the URL for the object you uploaded in this task and access it using a browser, you should get an access denied error
* Do not store sensitive information in a bucket that has public access.
* Do not turn on versioning on this bucket, it will be difficult to delete.

## Prerequisite

- What is Simple Storage Service (S3)? Amazon S3 is a global storage object platform that’s built to store, protect, and retrieve data from “buckets” at any time from anywhere on any device. Organizations of any size in any industry can use this service. Use cases include websites, mobile apps, archiving, data backups and restorations, IoT devices, enterprise application storage, and providing the underlying storage layer for your data lake. Runs from all regions and is a public service. 

- What is a bucket? Container for objects. Created in a specific AWS region. Name is globally unique. 

- What is object storage? You can't mount an S2 bucket. Object can be thought of a file that has two main components: object key - file name in a bucket & value - data or contents of the bucket. 

- How is object storage different than block storage? 
---> Block Storage is the data storage model with which most users are familiar. It is the easiest model to immediately grasp: your Microsoft Word documents, enterprise databases, and cat photos are all stored as files on a disk or array. These files have a beginning and end somewhere on one or more hard disks, and are chopped up into discrete units called Blocks. Each Block has an address that the Operating System knows, and that address is the only way to access that specific file (or piece of a file). 
---> S3 introduced a single storage unit, aptly named a “Bucket”. Buckets hold S3’s only data unit, the “Object”. To access Objects, the user needs only the following information:

* The Bucket URL

* The Access Keys for the Bucket

* Metadata that applies to the Object, such as: Name, File Format, Custom Metadata Tags

- What is the maximum amount of data that you can store in an S3 bucket? A single Amazon S3 object can store from 0 bytes to a maximum of 5 terabytes. The largest object that can be uploaded in a single PUT is 5 gigabytes. The total volume that an s3 bucket can store is unlimited. If an object size is greater than 5gigabytes, you should consider multipart upload.

- What is the maximum file size you can store in an S3 bucket? The maximum file size that any object uploaded to S3 can be is 5 TB.

- By default, are objects in an S3 bucket public? By default, new S3 bucket settings do not allow public access, but customers can modify these settings to grant public access using policies or object-level permissions.

- What are the security best practices regarding S3 buckets? Block public S3 buckets at the organization level, Use bucket policies to verify all access granted is restrited and specific, ensure that any identity-based policies dont use wildcard actions, enable S3 protection in GuardDuty to detect suspcious activities, etc. 

- What is an S3 bucket policy? It's a resource policy but attached to resource (attached to bucket), controls who has access to that resource, can allow/deny access from different accounts, can allow/deny anonymous principals. 

- What are storage classes in S3? The S3 storage classes include S3 Intelligent-Tiering for automatic cost savings for data with unknown or changing access patterns; S3 Standard for frequently accessed data; S3 Standard-Infrequent Access (S3 Standard-IA) and S3 One Zone-Infrequent Access (S3 One Zone-IA) for less frequently accessed data; S3 Glacier Instant Retrieval for archive data that needs immediate access, S3 Glacier Flexible Retrieval (formerly S3 Glacier) for rarely accessed long-term data that does not require immediate access, and Amazon S3 Glacier Deep Archive (S3 Glacier Deep Archive) for long-term archive and digital preservation with retrieval in hours at the lowest cost storage in the cloud. If you have data residency requirements that can’t be met by an existing AWS Region, you can use the S3 Outposts storage class to store your S3 data on premises.

- How is a bucket policy different from an IAM policy?  IAM policies define what a principal can do in your AWS environment. S3 bucket policies, on the other hand, are attached only to S3 buckets. S3 bucket policies specify what actions are allowed or denied for which principals on the bucket that the bucket policy is attached to (e.g. allow user Alice to PUT but not DELETE objects in the bucket). S3 bucket policies are a type of access control list. 

## Steps

- Step 1 — Using the cli, create an S3 bucket name: day8-bucket123
    a. open terminal --> aws s3 mb s3://day8-bucket123

<img width="568" alt="1" src="https://user-images.githubusercontent.com/41940176/147517275-a3708aba-8a9c-4a9e-a750-2bcdd47e698d.png">

- Step 2 — Upload an object (any file) into the bucket. 
    a. You can send a PUT request to upload an object of up to 5 GB in a single operation
    b. Now copy a pic from your local disk to S3 bucket --> aws s3 cp [file on desktop] s3://day8-bucket123
    c. YOu should get something similar to this message: upload: ./fish.png to s3://day8-bucket123/fish.png

<img width="632" alt="2" src="https://user-images.githubusercontent.com/41940176/147517276-18e4b335-28ba-4410-89e6-bb25e26b6d9e.png">

- Step 3 — Delete the bucket when you are done: aws s3 rm s3://<unique-bucket-name>
<img width="632" alt="3" src="https://user-images.githubusercontent.com/41940176/147517277-718c4ba6-556a-49a1-86d2-95447587e12b.png">

## Social Proof

✍️ Show that you shared your process on Twitter or LinkedIn

[link](link)
