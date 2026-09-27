# Network Security — Phishing Detection Pipeline

An end-to-end machine learning pipeline that detects phishing websites/URLs, built with a production-style MLOps structure: data ingestion, validation, transformation, model training, and deployment via Docker.

## 🧩 Problem Statement
Phishing attacks remain one of the most common attack vectors in network security. This project builds a classifier that flags phishing attempts based on extracted URL/website features, and packages it as a deployable service.

## ⚙️ Pipeline Architecture
1. **Data Ingestion** (`push_data.py`) — loads and pushes raw data to MongoDB
2. **Data Validation** (`data_schema/`) — validates incoming data against an expected schema
3. **Data Transformation** — feature engineering / preprocessing
4. **Model Training** — trains and evaluates the classifier, best model saved to `final_model/`
5. **Serving** (`app.py`) — exposes the trained model for inference
6. **Orchestration** (`main.py`) — runs the pipeline end to end

## 🛠️ Tech Stack
- **Language:** Python
- **Database:** MongoDB
- **Deployment:** Docker, AWS EC2
- **CI/CD:** GitHub Actions (`.github/workflows`)

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- MongoDB instance (local or Atlas)
- Docker (for containerized deployment)

### Installation
\`\`\`bash
git clone https://github.com/123456-raul/networksecurity.git
cd networksecurity
pip install -r requirements.txt
\`\`\`

### Environment Variables
Create a `.env` file with your MongoDB connection string:
\`\`\`
MONGO_DB_URL=<your-mongodb-connection-string>
\`\`\`

### Run the Pipeline
\`\`\`bash
python main.py
\`\`\`

### Run the App
\`\`\`bash
python app.py
\`\`\`

### Docker Deployment (EC2)
\`\`\`bash
# On EC2 instance
sudo apt-get update -y && sudo apt-get upgrade -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker

# Build and run
docker build -t networksecurity .
docker run -p 8080:8080 networksecurity
\`\`\`

## 📁 Project Structure
\`\`\`
networksecurity/
├── networksecurity/      # core package (pipeline components)
├── data_schema/          # validation schema
├── Network_Data/         # raw/sample data
├── final_model/          # trained model artifacts
├── templates/            # app templates
├── app.py                # inference/serving app
├── main.py               # pipeline entry point
├── push_data.py          # data ingestion to MongoDB
├── Dockerfile
└── requirements.txt
\`\`\`

## 📌 Future Improvements
- Add model performance metrics/report to README
- Add CI/CD deployment status badge
- Add a live demo link if hosted
