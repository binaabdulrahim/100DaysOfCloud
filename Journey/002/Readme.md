![Pink Fun Cloud Mental Health Therapy Games Logo (1)](https://user-images.githubusercontent.com/41940176/147340937-89bd90d7-5096-40fe-943b-7bdc8551930a.gif)
# Create an IAM user

## Introduction

✍️ (Why) I picked this project to get started with creating an IAM user on console then replicate this via cli. 

## Prerequisite
- What is Identity and Access Management (IAM)? IAM is a web service that helps you securely control access to AWS resources. You use IAM to control who is authenticated (signed in) and authorized (has permissions) to use resources

- What is a root user? The credentials of the account owner allow full access to all resources in the account. You cannot use IAM policies to explicitly deny the root user access to resources. You can only use an AWS Organizations service control policy (SCP) to limit the permissions of the root user.

- How is a root user different from an Admin user? Instead, create a new IAM user for each person that requires administrator access. Then make those users administrators by placing the users into an "Administrators" user group to which you attach the AdministratorAccess managed policy. It is recommmended, do not use the AWS account root user for any task where it's not required.

- What is console access and programmatic access? The console is a browser-based interface to manage IAM and AWS resources. The IAM user might need to make API calls, use the AWS CLI, or use the Tools for Windows PowerShell. In that case, create an access key (access key ID and a secret access key) for that user.

- What is the access key and secret key? When you create your access keys, you create the access key ID (for example, AKIAIOSFODNN7EXAMPLE) and secret access key (for example, wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY) as a set. The secret access key is available for download only when you create it. If you don't download your secret access key or if you lose it, you must create a new one.

You can assign up to two access keys per user (root user or IAM user). Having two access keys is useful when you want to rotate them. When you disable an access key, you can't use it, but it counts toward your limit of two access keys. After you delete an access key, it's gone forever and can't be restored, but it can be replaced with a new access key.

- What is MFA and why is it important? You can add two-factor authentication to your account and to individual users for extra security. With MFA you or your users must provide not only a password or access key to work with your account, but also a code from a specially configured device.

- What are policies and how can you create them? A policy is an object in AWS that, when associated with an identity or resource, defines their permissions. AWS evaluates these policies when an IAM principal (user or role) makes a request. Permissions in the policies determine whether the request is allowed or denied. Most policies are stored in AWS as JSON documents. AWS supports six types of policies: identity-based policies, resource-based policies, permissions boundaries, Organizations SCPs, ACLs, and session policies.

- What are roles and how can you create them? IAM roles are identities that are used by a large group of individuals. It have more than 5000 principals, it could be a candiate for an IAM Role. Iam Roles are assumed you become that role. 

- What is the difference between a role and a policy? Roles have credentials that can be used to authenticate the Role identity. You can assign either a pre-built policy or create a custom policy. A policy is something that will be assigned to a role

- What is a user group? An IAM user group is a collection of IAM users. User groups let you specify permissions for multiple users, which can make it easier to manage the permissions for those users.

- What are some good security practices for password policies? The default password policy enforces the following conditions:Minimum password length of 8 characters and a maximum length of 128 characters. Minimum of three of the following mix of character types: uppercase, lowercase, numbers, and ! @ # $ % ^ & * ( ) _ + - = [ ] { } | ' symbols. Not be identical to your AWS account name or email address


<<<<<<< HEAD
### Via Console:
- Step 1 — Sign into root account. Search bar --> IAM --> Users --> Add users. Pick Access key so we can use it via CLI and API. Press Next.

![1](https://user-images.githubusercontent.com/41940176/147333276-03b1bba6-b7e6-4e5e-8bf9-d4c9d648c31b.png)

- Step 2 — Create group --> Group name: AdministratorAccess managed policy to the new group --> create group --> next.

![2](https://user-images.githubusercontent.com/41940176/147333278-87a2b81a-9c6c-4f7f-9e3d-f5dd2887b5d0.png)

- Step 3 — Review page --> create user. 

![3](https://user-images.githubusercontent.com/41940176/147333280-fe1afd5c-b237-4cbf-84cd-c944c3161b21.png)

- Step 4 — Download the .csv file. Make sure to keep it somewhere safe. Because we are going to use this to login via CLI.

![4](https://user-images.githubusercontent.com/41940176/147333282-0d0c8175-3441-4067-a3f3-4e864286fd28.png)

- Step 5 — Click on AWS Console Home --> Right side click on your account --> Security Credentials --> 

![5](https://user-images.githubusercontent.com/41940176/147334437-5a63a339-b510-400c-b565-6dac03107644.png)

- Step 6 — Multi-Factor Authentication --> Activate MFA -> Virtual MFA device --> Follow instructions and download QR code --> Assign MFA. 

### Via Cli:

- Step 1 — In Console section, we create an admin user called CloudSec and downloaded the csv file. Open the csv file and open your terminal. In terminal, download aws cli. Then type: aws configure --profile CloudSec --> here is where the information from the csv file goes. 

- Step 2 — To verify that the step was done correctly. Type aws s3 ls --profile CloudSec. If you dont have any s3 buckets, you will not see anything but thats fine. 
=======


## Social Proof

[link](link)
