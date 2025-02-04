Credit Fraud Detection Project
This is a full-stack project for detecting credit card fraud using machine learning. It consists of:
•	Backend: FastAPI-based API for training and predicting fraud detection.
•	Frontend: A React-based UI for users to upload CSV files and view predictions.
•	Docker: The entire app is containerized using Docker and orchestrated with docker-compose.
________________________________________
📂 Project Structure
app/
│── backend/               # Backend API (FastAPI)
│   ├── main.py            # Main FastAPI application
│   ├── model.py           # Model training & prediction logic
│   ├── requirements.txt   # Dependencies for backend
│   ├── Dockerfile         # Backend Docker setup
│
│── frontend/              # Frontend React App
│   ├── src/
│   │   ├── App.tsx        # Main React UI
│   │   ├── api.ts         # API integration
│   ├── package.json       # Dependencies for frontend
│   ├── Dockerfile         # Frontend Docker setup
│
│── docker-compose.yml     # Docker Compose setup
│── README.md              # Documentation
________________________________________
🖥️ Backend (FastAPI)
The backend provides an API to train a model and predict fraudulent transactions.
Installation & Running Locally
cd backend
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
API Endpoints
Method	Endpoint	Description
POST	/upload/	Upload CSV file for training
POST	/predict/	Predict if a transaction is fraud
________________________________________
🌐 Frontend (React)
The frontend provides a UI to upload transaction data and visualize predictions.
Installation & Running Locally
cd frontend
npm install
npm start
Features
•	File upload to send data to the backend.
•	Displays fraud predictions.
________________________________________
🐳 Docker Setup
The project is fully containerized. You can run both backend and frontend using Docker.
Build & Run with Docker Compose
docker-compose up --build
Access the services
•	Backend: http://localhost:8000
•	Frontend: http://localhost:3000
________________________________________
🚀 Deployment (Optional)
You can deploy the backend and frontend using Docker on a cloud service (AWS, GCP, DigitalOcean, etc.).
Deploy with Docker
docker build -t credit-fraud-backend ./backend

docker build -t credit-fraud-frontend ./frontend

docker run -p 8000:8000 credit-fraud-backend

docker run -p 3000:3000 credit-fraud-frontend
________________________________________
📌 To-Do
•	
________________________________________
📜 License
This project is licensed under the MIT License.
🎯 Contributions
Feel free to fork this repository and submit pull requests! 🚀

