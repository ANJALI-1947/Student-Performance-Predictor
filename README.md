# 🎓 Student Performance Predictor

## Overview

Student Performance Predictor is a Machine Learning web application that predicts a student's math score based on academic and demographic features. The project uses Linear Regression and provides real-time predictions through a Flask-based web interface.

---

## Application Screenshot

![Student Performance Predictor](images/screenshot.png)

---

## Features

- Predicts student math scores using Machine Learning
- Real-time prediction through a web interface
- Data preprocessing and feature encoding
- Linear Regression model training and evaluation
- Flask integration for deployment
- Clean and responsive UI

---

## Technologies Used

### Machine Learning
- Python
- Pandas
- NumPy
- Scikit-Learn

### Web Development
- Flask
- HTML
- CSS

### Tools
- VS Code
- Git
- GitHub

---

## Dataset

The project uses the Student Performance Dataset containing:

- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score
- Math Score

### Target Variable

**Math Score**

---

## Machine Learning Workflow

1. Data Collection
2. Data Exploration
3. Data Preprocessing
4. Feature Encoding
5. Feature Selection
6. Train-Test Split
7. Linear Regression Model Training
8. Model Evaluation
9. Model Saving using Pickle
10. Flask Integration

---

## Model Performance

| Metric | Score |
|----------|----------|
| Mean Absolute Error (MAE) | 4.19 |
| R² Score | 0.88 |

---

## Project Structure

StudentPerformancePredictor/

├── data/

├── model/

├── static/

├── templates/

├── images/

├── train.py

├── app.py

├── requirements.txt

└── README.md

---

## Installation and Setup

### Clone Repository

```bash
git clone <repository-url>
cd StudentPerformancePredictor
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## Learning Outcomes

- Data preprocessing
- Feature engineering
- Machine Learning model training
- Model evaluation
- Flask web development
- Git and GitHub workflow
- End-to-end ML application development

---

## Author

**Anjali Kumari**