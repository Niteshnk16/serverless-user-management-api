# 🚀 Serverless User Management API

This project is a Serverless REST API built using AWS Lambda, API Gateway, and Serverless Framework.

It demonstrates how to deploy a scalable backend without managing servers.

---

## 📌 Features
- Serverless architecture (no server management)
- Fast and scalable API
- Easy deployment using Serverless Framework
- Cloud-based backend using AWS

---

## 🛠 Tech Stack
- AWS Lambda
- API Gateway
- Serverless Framework
- Python

---

## 📡 API Endpoints

GET https://2bnrvw4we4.execute-api.us-east-2.amazonaws.com/hello  
GET https://2bnrvw4we4.execute-api.us-east-2.amazonaws.com/bye

---

## 📥 Sample Response
{
  "message": "Go Serverless v4.0! Your function executed successfully!"
}

---

## ⚙️ Setup & Deployment

Install Serverless:
npm install -g serverless

Configure AWS:
aws configure

Deploy project:
sls deploy

---

## 🧪 Test API
GET https://2bnrvw4we4.execute-api.us-east-2.amazonaws.com/hello  
GET https://2bnrvw4we4.execute-api.us-east-2.amazonaws.com/bye

---

## 📂 Project Structure
- handler.py → Lambda function code  
- serverless.yml → configuration file  
- README.md → project documentation  

---

## 🚀 Future Improvements
- Add database (DynamoDB)
- Add POST/PUT APIs
- Add authentication
- CI/CD integration (GitHub Actions)

---

## 👨‍💻 Author
Nitesh Kumar
