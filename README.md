# QUEUELESS AI
### Intelligent Queue Prediction and Management System

QUEUELESS AI is an AI-powered queue management web application designed to simplify customer queue handling, estimate waiting times, and improve service efficiency through intelligent automation.

The system combines Machine Learning, Retrieval-Augmented Generation (RAG), Gemini AI, and QR-based token tracking to provide a smarter queue management experience.

---

## Project Overview

Traditional queue management systems often require customers to wait without knowing their estimated waiting time or current queue status.

QUEUELESS AI addresses this challenge by providing a digital token management system with intelligent waiting-time prediction, AI-powered recommendations, and QR-based token tracking.

The application provides separate interfaces for customers and administrators to manage and monitor queue operations.

## Key Features

- **Digital Token Generation:** Generate unique tokens for customers.
- **QR Code Integration:** Generate QR codes for individual tokens and access token tracking.
- **Queue Management:** Manage waiting, serving, and completed tokens.
- **Machine Learning Prediction:** Estimate customer waiting time based on queue information.
- **Gemini AI Integration:** Generate intelligent queue analysis and recommendations.
- **RAG-Based Knowledge Retrieval:** Retrieve relevant queue management information to support AI responses.
- **Live Dashboard:** Monitor queue statistics and service activity.
- **Admin Dashboard:** Manage queue operations and monitor customer tokens.
- **CSV Export:** Export queue information for further analysis.
- **User Authentication:** Separate customer and administrator access.

## Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Backend | Flask |
| Frontend | HTML, CSS, JavaScript |
| Database | SQLite |
| Artificial Intelligence | Google Gemini API |
| Machine Learning | Scikit-learn, NumPy, Pandas |
| Knowledge Retrieval | RAG |
| QR Code | Python QR Code Library |
| Data Visualization | Chart.js |
| Development Environment | Visual Studio Code |

## Project Architecture

```text
QUEUELESS AI
     |
     v
Flask Web Application
     |
     +----------------------+
     |                      |
 Customer Interface    Admin Dashboard
     |                      |
     v                      v
Token Generation       Queue Monitoring
     |                      |
     v                      v
QR Code Tracking      ML Prediction
                            |
                            v
                      RAG Knowledge
                            |
                            v
                       Gemini AI
                            |
                            v
                  Intelligent Insights
```

## Project Structure

```text
QUEUELESS_AI/
│
├── app.py
├── agents.py
├── database.py
├── feature_setup.py
├── live_routes.py
├── ml_prediction.py
├── nexus_api.py
├── prediction.py
├── qr_routes.py
├── rag.py
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── user.html
│   ├── admin.html
│   ├── track.html
│   └── 404.html
│
├── static/
│   ├── style.css
│   ├── script.js
│   └── live.js
│
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Directory

```bash
cd QUEUELESS_AI
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a `.env` file in the project root directory using `.env.example` as a reference.

Configure the required values:

```env
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=your_model_name
FLASK_SECRET_KEY=your_secret_key
ADMIN_USERNAME=your_admin_username
ADMIN_PASSWORD=your_admin_password
```

**Important:** Never upload your actual `.env` file, API key, or passwords to GitHub.

### 7. Run the Application

```bash
python app.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000/
```

## Application Modules

**1. User Management**

Allows customers to register, log in, generate tokens, and track their queue status.

**2. QR-Based Token Tracking**

Provides QR codes associated with customer tokens for convenient tracking.

**3. Queue Monitoring**

Tracks waiting, serving, and completed customers.

**4. Machine Learning Prediction**

Estimates waiting time based on queue-related information.

**5. AI Recommendation Agent**

Uses Gemini AI to generate queue analysis and operational recommendations.

**6. RAG Knowledge Retrieval**

Retrieves relevant knowledge to provide context for AI-generated responses.

**7. Admin Dashboard**

Provides queue statistics, token management, AI insights, and CSV export functionality.

## Security Considerations

- Store API keys and secret credentials in environment variables.
- Exclude `.env`, database files, and virtual environments from version control.
- Use strong administrator credentials.
- Avoid exposing sensitive customer information.
- Use HTTPS and appropriate security configurations before public deployment.

## Future Enhancements

- Cloud-based deployment.
- Advanced queue forecasting.
- SMS and email notifications.
- Multiple service counter support.
- Advanced analytics and reporting.
- Improved mobile accessibility.

## Learning Outcomes

This project demonstrates practical implementation of:

- Python web application development.
- Machine Learning integration.
- Generative AI and API integration.
- RAG-based knowledge retrieval.
- Database management.
- QR code generation and tracking.
- Frontend and backend integration.

## Author

**Dhivya**

B.Tech – Information Technology

## Project Title
QUEUELESS AI – Intelligent Queue Prediction and Management System

Developed as an academic project to explore the integration of Artificial Intelligence, Machine Learning, and web technologies for intelligent queue management.

**QUEUELESS AI – Intelligent Queue Prediction and Management System**

---

*Developed as an academic project to explore the integration of Artificial Intelligence, Machine Learning, and web technologies for intelligent queue management.*
