# Breast Cancer Prediction App

This project is a machine learning web application that predicts whether a breast tumor is malignant or benign based on user-provided input. It uses a logistic regression model trained on the Breast Cancer Wisconsin dataset and is deployed using Flask and Heroku.

## 🔍 Project Overview

- **Model**: Logistic Regression trained on top 4 correlated features
- **Dataset**: Breast_Cancer_Data.csv (from previous module)
- **Deployment**: Flask API hosted on Heroku
- **Frontend**: HTML form for user input
- **Backend**: Python model served via Flask
- **Live App**: [Heroku Link](https://ana680-wk2-hw-89bc327fe664.herokuapp.com/)

## 📁 Repository Structure

```
├── app.py                      # Flask application logic
├── breast_cancer_model.pkl     # Saved ML model
├── requirements.txt            # Python dependencies
├── Procfile                    # Heroku process declaration
├── .python-version             # Python version for Heroku
├── templates/
│   └── index.html              # User input form
├── ANA 680 WK 2 Assg.ipynb     # Model training and feature selection
```


## 🚀 How to Run Locally

1. Clone the repo  
2. Create a virtual environment  
3. Install dependencies: `pip install -r requirements.txt`  
4. Run the app: `python app.py`  
5. Visit `http://localhost:5000` in your browser

## 🧠 Model Details

- Selected top 4 features based on correlation with diagnosis
- Trained using logistic regression for interpretability
- Saved using `pickle` for deployment

## 🔧 Deployment Notes

- Hosted on Heroku using Git and CLI
- Requirements file must be named `requirements.txt`
- Procfile must declare: `web: gunicorn app:app`

## 📎 Links

- [GitHub Repository](https://github.com/Daniel-Kast/ANA-680-HW)
- [Live Heroku App](https://ana680-wk2-hw-89bc327fe664.herokuapp.com/)
