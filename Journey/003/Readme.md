**Add a cover photo like:**
![placeholder image](https://via.placeholder.com/1200x600)

# Use a managed Config Rule

## Introduction

✍️ (Why) Explain in one or two sentences why you choose to do this project or cloud topic for your day's study.

## Prerequisite

- What is AWS Config? Provides an inventory of AWS resources and a history of configureation changes to these resources. By using AWS Config to evaluate your resource configurations, you can assess how well your resource configurations comply with internal practices, industry guidelines, and regulations. You can create up to 250 AWS Config rules per region in your account.

- What does an AWS Config rule do? Use AWS Config to evaluate the configuration settings of your AWS resources. You do this by creating AWS Config rules, which represent your ideal configuration settings. AWS Config provides customizable, predefined rules called managed rules to help you get started. While AWS Config continuously tracks the configuration changes that occur among your resources, it checks whether these changes violate any of the conditions in your rules. If a resource violates a rule, AWS Config flags the resource and the rule as noncompliant.

- What is remediation in the context of a config rule? When you apply a remediation action to an AWS Config rule violation, automation is initiated when the rule violation is detected. When AWS Config detects a change, it can trigger a change request to remediate the issue. The change request can be configured to make the change as soon as possible or within the next available maintenance window based on the change calendar. You can also configure change approvals to assure that the change is appropriate



- Step 1 — Turn on AWS Config in the US-EAST-1 region
      a. On AWS Console --> Search bar --> AWS Config -> Get Started. Make sure you're in US-EST-1 
<img width="700" alt="1" src="https://user-images.githubusercontent.com/41940176/147338131-e483da29-f971-45bf-b941-0ad6dfed1fe2.png">

- Step 2 — Setting
      a. Set the kind of resources you want to record. Remember this is not included in free tier. 
      b. Anytime, we have a change, we can log that change in a S3 bucket called config-bucket ####
      c. Click on Next
![2](https://user-images.githubusercontent.com/41940176/147338133-55fac6d5-b346-448d-9320-4647d46a70ef.png)

- Step 3 — Choose the managed Config rule eg. encrypted-volumes
      a. There is a lot of rules to pick from. These rules allow track compliance of AWS resources. 
      b. Click next and review. Submit.

![3](https://user-images.githubusercontent.com/41940176/147338134-df6be82a-73c1-4708-9537-916117ae74f2.png)
![4 a](https://user-images.githubusercontent.com/41940176/147338135-aededca0-4188-4f76-aa2f-3600db0790bc.png)

- Step 4 — Launch an EC2 instance without an encryped EBS volume
      a. Search bar --> EC2 Instance
      b. Launch EC2 Instance --> Click Launch
      c. Under storage, we can see that our EC2 instance is not encrypted. 
      
![5](https://user-images.githubusercontent.com/41940176/147338137-5c2e97a5-d245-4a5b-b99b-2ae5c85db3d4.png)
![5 z](https://user-images.githubusercontent.com/41940176/147338139-ebf2d9b8-8a4b-4712-bba2-6201c0ba61f2.png)


- Step 5 — Monitor AWS Config until it detects there is an EBS volume that is unencrpyted
      a. Search bar --> Config Dashboard
      b. Here you can see total resrouces. 
      c. Under Compliance status --> 1 Noncompliant Resource --> Unencrypted EBS EC2 that we just created. 
![6](https://user-images.githubusercontent.com/41940176/147338141-bba9fbd8-81ae-4358-97fb-ca84b45f6d58.png)
![6a](https://user-images.githubusercontent.com/41940176/147338142-050fb5a2-641e-41d1-a41a-02250bec3a58.png)


- Step 5 — Delete aws config and EC2 instance.

## Social Proof

✍️ Show that you shared your process on Twitter or LinkedIn

[link](link)

  
