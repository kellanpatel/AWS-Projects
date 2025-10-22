# AWS Projects

This repository contains two small projects built to explore cloud deployment and automation using AWS.

---

## 🌍 Website – AWS CI/CD Deployment Demo
A static website hosted on **Amazon S3** and delivered globally through **Amazon CloudFront**.  
The site is automatically deployed using a **CI/CD pipeline** built with **AWS CodePipeline** connected to **GitHub**.  
Whenever code is pushed from **Visual Studio** to GitHub, AWS automatically updates the live website.

### ✨ Features
- Static website (HTML, CSS, JS)
- Hosted on Amazon S3
- Distributed globally via CloudFront (CDN + HTTPS)
- Automated deployment using AWS CodePipeline
- Source control managed through GitHub

### 🛠️ Tech Stack
- **AWS S3** – Website hosting  
- **AWS CloudFront** – Global content delivery  
- **AWS CodePipeline** – Continuous deployment automation  
- **GitHub** – Source control and integration trigger  
- **Visual Studio** – Local development environment  

### 🚀 How It Works
1. Edit code locally in Visual Studio.  
2. Commit and push changes to GitHub.  
3. AWS CodePipeline detects the update and deploys automatically to S3.  
4. CloudFront refreshes the cached version and serves the latest site globally.

🔗 **Live Website:** [https://kellan-portfolio.s3.eu-north-1.amazonaws.com/Website/index.html](https://kellan-portfolio.s3.eu-north-1.amazonaws.com/Website/index.html)
🔗 **Code Folder:** [`/Website`](./Website)

---

## 🧩 To-Do List App (In Development)
A work-in-progress web app to explore connecting AWS services (such as DynamoDB) with a simple front end.  
Currently, this folder contains scaffolding for future development.

🔗 **Code Folder:** [`/To-Do List App`](./To-Do%20List%20App)

---

## 💡 Skills Demonstrated
- AWS (S3, CloudFront, CodePipeline, IAM)  
- CI/CD automation  
- Git & GitHub workflows  
- Web hosting and deployment  
- Cloud architecture fundamentals  

---

Built by **Kellan Patel**
