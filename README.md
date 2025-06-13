# AWS S3 Event-Driven Notification System

This project implements a serverless event-driven architecture using AWS services. It monitors an S3 bucket for object creation events, triggers a Lambda function, and sends email notifications using SNS (Simple Notification Service).

![image](https://github.com/user-attachments/assets/8752f15a-2954-48fd-aceb-cca8bd5f89d8)

## 🧰 Tech Stack

- AWS S3 (Simple Storage Service)
- AWS Lambda
- AWS SNS
- AWS CloudWatch
- AWS IAM
- AWS CLI

## 🚀 Architecture

1. An object is uploaded to the S3 bucket.
2. S3 triggers the Lambda function via event notification.
3. Lambda processes the event and publishes a message to an SNS topic.
4. SNS sends an email notification to subscribed recipients.

## 📝 Features

- Real-time notifications for new S3 object uploads.
- Fully serverless and event-driven.
- S3 bucket versioning enabled for safe object management.
- CloudWatch logging for monitoring Lambda executions.

## 🔐 IAM Roles and Permissions

- Lambda execution role with:
  - `AWSLambdaBasicExecutionRole` (for CloudWatch logging)
  - `sns:Publish` permission for SNS topic access

## 🔧 Deployment Steps

1. Create S3 bucket with versioning enabled.
2. Create SNS topic and subscribe email.
3. Create IAM role for Lambda with appropriate permissions.
4. Deploy Lambda function with S3 trigger.
5. Upload objects to S3 and monitor email notifications.

Create a sample Cloud Formation template for creating the S3 bucket.
![image](https://github.com/user-attachments/assets/2e6e5333-4705-4d5e-9f97-4adacca9fee3)

Now Create the priavte instance to access the S3 bucket for good security.
Create a VPC with
1. Two Subnets (Public and Private).
2. Internet Gateway to access the external network.
3. NAT Gateway for to connect to the internet to allow private instances to initiate outbound traffic.
![image](https://github.com/user-attachments/assets/248c1f26-3c56-4c63-963d-9c1d03f67f59)

Now create two EC2 instances one with the Public subnet and other with Private subnet.
![image](https://github.com/user-attachments/assets/29e8787e-16d9-4d3e-83f0-739f5ffb886c)

Now ssh into priavte instance through the public instance wich is attached with public subnet.
![image](https://github.com/user-attachments/assets/34e78c4e-d212-47b7-a979-2e1e028c26b9)

login into the Private isntance and configure aws keys to access the aws CLI (Command Line Interfce)
![image](https://github.com/user-attachments/assets/eacd95a3-27b4-46e1-a712-b483a10684e1)

Creating a lambda function to triiger when an object is uploaded in the bucket.
![image](https://github.com/user-attachments/assets/309e5f18-2583-4d63-9e2b-b7467d8a3e93)

Also, attach a policy to allows Lambda function to publish messages only to SNS topic, following least privilege principle.
![image](https://github.com/user-attachments/assets/9faf1ff4-3cde-48a2-95ad-d22e7416d922)

![image](https://github.com/user-attachments/assets/472b394f-60d4-427f-99e0-7d66355285e9)


A destination is created for the lambda function with SNS to get notified about the object uploaded in the bucket.
![image](https://github.com/user-attachments/assets/a702fc19-b168-4c65-a0e1-439e200ab275)

Upload the new object in S3 through CLI 
![image](https://github.com/user-attachments/assets/190293ed-7766-4092-936c-1cd8e19107b5)


A notification sent to registred email in SNS topic about the object uploaded in the bucket.
![image](https://github.com/user-attachments/assets/83f9fce3-3c34-4ac7-8bf5-b8d0e662522f)

Cloudwatch log about the lambda invocation. 
![image](https://github.com/user-attachments/assets/8c176922-efd0-4251-9fe4-fd629bbaf806)


Checking the versions to check the retriving of the objects.
delete the object in the bucket.
![image](https://github.com/user-attachments/assets/a7faa00e-2fbb-4b0d-9c2c-25930486ab02)

Check the versions of the deleted object.
The  original file version is displayed followed by file exists in S3 but not visible because latest is a delete marker.
![image](https://github.com/user-attachments/assets/4aacd4f2-f229-401f-b0a1-bdd315faf67a)

Restoring the object with the help version ID.
![image](https://github.com/user-attachments/assets/f14d0f6d-966b-4ffa-b5df-43cdee07e06f)



