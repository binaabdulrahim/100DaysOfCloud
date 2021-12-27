![Pink Fun Cloud Mental Health Therapy Games Logo (1)](https://user-images.githubusercontent.com/41940176/147340937-89bd90d7-5096-40fe-943b-7bdc8551930a.gif)

# Install & Configure AWS CLI then create an S3 Bucket

## Introduction

- An overview of working with the AWS S3 bucket using CLI commands. We also look at a brief overview of the S3 bucket and its key components.

## Prerequisite

- How are permissions granted to IAM users? IAM users are identities in the service. When you create an IAM user, they can't access anything in your account until you give them permission. You give permissions to a user by creating an identity-based policy, which is a policy that is attached to the user or a group to which the user belongs.

- What credentials are created when configuring AWS locally and where are they stored? Run aws configure to quickly set and view your credentials, region, and output format. The AWS CLI stores this information in a profile (a collection of settings) named default in the credentials file. By default, the information in this profile is used when you run an AWS CLI command that doesn't explicitly specify a profile to use.

- What is the difference between s3 and s3api Commands? The s3 commands are a custom set of commands specifically designed to make it even easier for you to manage your S3 files using the CLI. The main difference between the s3 and s3api commands is that the s3 commands are not solely driven by the JSON models. Rather, the s3 commands are built on top of the operations found in the s3api commands. As a result, these commands allow for higher-level features that are not provided by the s3api commands. This includes, but is not limited to, the ability to synchronize local directories and S3 buckets, transfer multiple files in parallel, stream files, and automatically handle multipart transfers. In short, these commands further simplify and further quicken the transferring of files to, within, and from S3

## Steps

- Step 1 — Create an IAM user with a programmatic access type (and Administrator Access) if you do not have one already
    a. Sign into root account. Search bar --> IAM --> Users --> Add users. Pick Access key so we can use it via CLI and API. Press Next.

            ![1](https://user-images.githubusercontent.com/41940176/147333276-03b1bba6-b7e6-4e5e-8bf9-d4c9d648c31b.png)
    b. Create group --> Group name: AdministratorAccess managed policy to the new group --> create group --> next.

            ![2](https://user-images.githubusercontent.com/41940176/147333278-87a2b81a-9c6c-4f7f-9e3d-f5dd2887b5d0.png)

    c. Review page --> create user. 

            ![3](https://user-images.githubusercontent.com/41940176/147333280-fe1afd5c-b237-4cbf-84cd-c944c3161b21.png)

    d. Download the .csv file. Make sure to keep it somewhere safe. Because we are going to use this to login via CLI.

            ![4](https://user-images.githubusercontent.com/41940176/147333282-0d0c8175-3441-4067-a3f3-4e864286fd28.png)

- Step 2 — Install AWS CLI on MACOS Apple Silicon
    a. Open Terminal and install brew: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    b. Install Pip: curl -O https://bootstrap.pypa.io/get-pip.py
    c. Run script with python to install latest version of pip: python3 get-pip.py --user
    d. Install AWS CLI on terminal using pip: pip3 install awscli --upgrade --user 
    e. Verify that AWS CLI is installed: aws --verison 

- Step 3 — Configure AWS credentials locally: aws configure
    a. On terminal: aws configure 
    b. Open the csv file
    c. Input the Access key --> enter --> inpute Secret Access key --> enter --> US-EAST-1 --> enter --> enter again. Now you're done!

- Step 4 — Create an S3 bucket: aws s3 mb s3://<unique-bucket-name>
    a. On terminal input the following command to list out all the s3 buckets: aws s3 ls 
    b. Create an s3 bucket with name:day3-bucket and specify the region: aws s3 mb s3://day11-bucket --region us-east-1
![1](https://user-images.githubusercontent.com/41940176/147354270-ad7bb737-77ab-4acd-8a67-ca318aee9f06.png)

- Step 5 — Check the bucket was created: aws s3 ls

- Step 6 — Delete the bucket when you are done: aws s3 rb s3://<unique-bucket-name>
![2](https://user-images.githubusercontent.com/41940176/147354271-8799178c-65b7-40ba-9a43-a1b473a9d5ed.png)

✍️ Show that you shared your process on Twitter or LinkedIn

[link](link)
