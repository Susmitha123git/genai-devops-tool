GenAI DevOps Chatbot API:

### 🚀 Project Demo
<p align="center">
  <strong>API Request & Response:</strong><br>
  <img src="https://github.com/user-attachments/assets/4659cc3f-6315-4b1c-a244-bce2c498d3b1" width="100%" />
</p>

<p align="center">
  <strong>Deployment Logs:</strong><br>
  <img src="https://github.com/user-attachments/assets/e8c8e4c5-bd59-47f2-976e-50d91e2fd90a" width="100%" />
</p>

This project is a high-performance Chatbot API built with FastAPI and powered by Groq (Llama 3).
It is fully containerised using Docker and features an automated CI/CD pipeline via GitHub Actions.

Architecture:
Language: Python 3.11
Framework: FastAPIAI 
Engine: Llama-3.1-8b-instant (via Groq Cloud)
Containerization: Docker
Infrastructure: AWS EC2 (t2.micro)


How to Run
Prerequisites:Docker installed on your machine or server.
A Groq API Key 

Installation & DeploymentC
clone this repository and run the following commands:

In bash
# Build the Docker image
docker build -t genai-chatbot .

# Run the container
docker run -d -p 8000:8000 \
  --name chatbot-container \
  -e GROQ_API_KEY='your_actual_groq_key_here' \
  genai-chatbot

API Demo (Proof of Work)To test the chatbot, 
send a POST request to the /chat endpoint.
Command:
curl -X POST "http://localhost:8000/chat?prompt=Explain+DevOps+in+one+sentence"

"response":
"DevOps is a collaborative practice that combines software development (Dev) and IT operations (Ops) to improve the speed, quality, and reliability of software releases by aligning development and operations teams through shared practices, tools, and cultures."

DevOps Features
Dockerized: The application is completely isolated and portable.
Environment Management: Uses Environment Variables for secure API key handling.
CI/CD: Every push to the main branch triggers a GitHub Action to verify code integrity.
Cloud Hosted: Deployed on AWS EC2.
demonstrating real-world cloud infrastructure management and security group configuration

 Monitoring & Optimization
 Used docker stats to monitor resource consumption and ensured a lightweight image by pruning unnecessary libraries from the build process.
