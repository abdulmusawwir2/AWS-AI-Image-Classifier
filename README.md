# AWS AI Image Classifier

An end-to-end serverless AI-powered image classification system built using AWS cloud services. This project allows users to upload images through a frontend application, automatically stores the image in Amazon S3, analyzes the image using Amazon Rekognition AI, and stores detected labels in DynamoDB.

---

# Project Overview

This project demonstrates how modern AWS cloud services communicate together in an event-driven architecture.

The application workflow:

1. User uploads an image from frontend
2. API Gateway receives request
3. Lambda function uploads image to S3
4. S3 triggers another Lambda automatically
5. Amazon Rekognition analyzes image
6. AI labels are stored in DynamoDB
7. Frontend displays uploaded image successfully

---

# Features

* AI-based image recognition
* Serverless architecture
* Event-driven workflow
* Image upload using frontend UI
* Automatic AI analysis using Rekognition
* Image metadata storage in DynamoDB
* Fully hosted on AWS
* Scalable cloud-native architecture

---

# AWS Services Used

| Service            | Purpose                      |
| ------------------ | ---------------------------- |
| Amazon S3          | Store uploaded images        |
| AWS Lambda         | Backend serverless functions |
| Amazon API Gateway | Public API endpoint          |
| Amazon Rekognition | AI image analysis            |
| Amazon DynamoDB    | Store AI labels/results      |
| IAM                | Permissions and security     |
| CloudWatch         | Logs and monitoring          |

---

# Architecture Diagram

```text
Frontend (HTML/CSS/JS)
        ↓
API Gateway
        ↓
uploadImageFunction (Lambda)
        ↓
Amazon S3 Bucket
        ↓
S3 Event Notification
        ↓
analyzeImageFunction (Lambda)
        ↓
Amazon Rekognition
        ↓
Amazon DynamoDB
```

---

# Project Workflow Detailed Explanation

## Step 1 — Frontend Upload

The frontend allows the user to choose an image file and upload it.

JavaScript converts the image into Base64 format using FileReader.

```javascript
const reader = new FileReader();
```

The frontend sends a POST request to API Gateway.

---

## Step 2 — API Gateway

API Gateway acts as the public entry point of the backend.

It receives the HTTP POST request and triggers the first Lambda function.

Configured Route:

```text
POST /upload
```

---

## Step 3 — uploadImageFunction Lambda

This Lambda function:

* Receives image data
* Decodes Base64 image
* Generates unique image filename
* Uploads image into S3 bucket

Main AWS SDK function used:

```python
s3.put_object()
```

---

## Step 4 — Amazon S3

Amazon S3 stores uploaded images securely.

Whenever a new image is uploaded:

```text
Object Created Event
```

is automatically generated.

---

## Step 5 — S3 Event Notification

S3 automatically triggers the second Lambda function.

Configured Trigger:

```text
Object Created → analyzeImageFunction
```

This is event-driven architecture.

---

## Step 6 — analyzeImageFunction Lambda

This Lambda function:

* Receives uploaded image metadata from S3
* Reads image from S3 bucket
* Calls Amazon Rekognition
* Extracts detected labels
* Stores results in DynamoDB

Main Rekognition API:

```python
rekognition.detect_labels()
```

---

## Step 7 — Amazon Rekognition

Amazon Rekognition is AWS AI service for image and video analysis.

It detects:

* Animals
* Objects
* Vehicles
* Nature
* Faces
* Text
* Scenes

Example labels:

```text
Tiger
Animal
Wildlife
Mammal
```

---

## Step 8 — DynamoDB

Detected labels are stored in DynamoDB.

Example stored item:

```json
{
  "image_id": "abc123.jpg",
  "labels": ["Tiger", "Animal", "Wildlife"]
}
```

---

# Folder Structure

```text
project/
│
├── index.html
├── uploadImageFunction.py
├── analyzeImageFunction.py
└── README.md
```

---

# Frontend Technologies

* HTML
* CSS
* JavaScript

---

# Backend Technologies

* Python 3.12
* AWS Lambda
* boto3 SDK

---

# Lambda Functions

## 1. uploadImageFunction

### Purpose

Uploads image into S3 bucket.

### Trigger

API Gateway HTTP POST request.

### Responsibilities

* Receive image data
* Decode Base64
* Generate image ID
* Upload image to S3

---

## 2. analyzeImageFunction

### Purpose

Analyze uploaded image using AI.

### Trigger

S3 Object Created Event.

### Responsibilities

* Read image metadata
* Call Rekognition
* Extract labels
* Store results in DynamoDB

---

# API Endpoint

```text
POST /upload
```

Example Request:

```json
{
  "image": "base64ImageData"
}
```

Example Response:

```json
{
  "message": "Upload successful",
  "image_id": "abc123.jpg"
}
```

---

# DynamoDB Table Structure

## Table Name

```text
ImageResults
```

## Attributes

| Attribute | Type   |
| --------- | ------ |
| image_id  | String |
| labels    | List   |

---

# IAM Permissions Used

The Lambda execution role includes:

* AmazonS3FullAccess
* AmazonRekognitionFullAccess
* AmazonDynamoDBFullAccess
* AWSLambdaBasicExecutionRole

---

# Security Considerations

* Private S3 image storage bucket
* IAM role-based permissions
* No hardcoded AWS credentials
* CORS enabled for frontend requests

---

# Challenges Faced

## 1. CORS Errors

Frontend requests were blocked by browser because API Gateway CORS configuration was missing.

### Solution

Configured:

```text
Access-Control-Allow-Origin: *
```

in API Gateway and Lambda response headers.

---

## 2. S3 Trigger Issues

Some uploaded images were not appearing in DynamoDB.

### Solution

Decoded S3 object key using:

```python
urllib.parse.unquote_plus()
```

---

# Deployment

Frontend deployed using:

```text
Amazon S3 Static Website Hosting
```

Backend services:

* API Gateway
* Lambda
* Rekognition
* DynamoDB

are fully hosted on AWS cloud.

---

# Future Improvements

* Display AI labels directly on frontend
* Add confidence percentage
* Add authentication system
* Add drag-and-drop upload
* Add image history dashboard
* Add React frontend
* Add CI/CD pipeline
* Add CloudFront CDN
* Add custom domain

---

# Learning Outcomes

This project helped in understanding:

* Serverless architecture
* Event-driven systems
* AWS Lambda
* API Gateway integration
* S3 object storage
* AI service integration
* DynamoDB operations
* IAM permissions
* Cloud deployment
* Debugging cloud applications

---

# Resume Description

Developed a serverless AI-powered image classification system using AWS Lambda, Amazon S3, API Gateway, Rekognition, and DynamoDB. Implemented event-driven arc
