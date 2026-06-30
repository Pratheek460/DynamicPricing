AI Dynamic Pricing & Demand Forecasting Platform

An AI-powered retail analytics platform that predicts future product demand, recommends optimal pricing strategies, estimates revenue, and helps businesses make smarter inventory decisions.

Built using FastAPI, XGBoost, and the Corporación Favorita Grocery Sales Forecasting dataset, this project demonstrates how machine learning can be applied to solve real-world retail and supply chain problems.

Project Overview

Retail businesses constantly face questions like:

How much inventory should we order?
Which products will have high demand next week?
Are we charging the right price?
How can we maximize profit without reducing sales?

This project provides a complete machine learning pipeline that answers these questions through demand forecasting and dynamic pricing.

The application processes historical sales data, engineers meaningful features, trains a forecasting model, and exposes predictions through a FastAPI backend with a simple web interface.

Features
 Forecast future product demand using machine learning
 Recommend optimal selling prices
 Estimate inventory reorder quantities
 Forecast expected revenue and profit
 Analyze products across multiple stores
 REST API built with FastAPI
 Interactive frontend using HTML, CSS and JavaScript
 Modular and scalable project structure
 
Technologies Used
Backend
FastAPI
Python
Pandas
NumPy
Scikit-learn
XGBoost
Joblib
Frontend
HTML
CSS
JavaScript
Dataset
Corporación Favorita Grocery Sales Forecasting (Kaggle)
Project Structure
DynamicPricing/

├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│
├── src/
│
│   ├── ingestion/
│   ├── features/
│   ├── forecasting/
│   ├── pricing/
│   ├── inventory/
│   ├── revenue/
│   ├── api/
│   └── frontend/
│
├── requirements.txt
└── README.md
Machine Learning Workflow

The project follows a complete end-to-end workflow:

Raw Sales Data
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
Demand Forecasting Model
        │
        ▼
Demand Prediction
        │
        ▼
Price Recommendation
        │
        ▼
Revenue Forecast
        │
        ▼
Inventory Optimization
Feature Engineering

To improve forecasting performance, the following features are generated from the raw dataset:

Lag Features (1, 7, 14 and 30 days)
Rolling Mean
Rolling Standard Deviation
Day of Week
Month
Quarter
Weekend Indicator
Holiday Indicator
Oil Price Information
Store Transactions
Store Metadata
Product Metadata

These engineered features allow the model to capture seasonal trends and purchasing behavior more effectively.

API Endpoints
Endpoint	Description
POST /predict-demand	Predict future product demand
POST /recommend-price	Recommend an optimal selling price
POST /inventory	Calculate inventory reorder quantity
POST /revenue	Estimate revenue and profit

Interactive API documentation is available through Swagger:

http://127.0.0.1:8000/docs
Dataset

This project uses the Corporación Favorita Grocery Sales Forecasting dataset from Kaggle.

The following files should be placed inside the data/raw/ directory:

train.csv
test.csv
stores.csv
items.csv
oil.csv
transactions.csv
holidays_events.csv
Running the Project
Clone the repository
git clone https://github.com/yourusername/DynamicPricing.git

cd DynamicPricing
Create a virtual environment
python3 -m venv venv

Activate it:

macOS / Linux

source venv/bin/activate

Windows

venv\Scripts\activate
Install dependencies
pip install -r requirements.txt
Prepare the dataset

Run the preprocessing pipeline:

python src/run_pipeline.py

Generate engineered features:

python src/build_features.py

Train the forecasting model:

python src/forecasting/train.py

Generate predictions:

python src/forecasting/predict.py
Start the API
uvicorn src.api.app:app --reload

Open:

http://127.0.0.1:8000/docs
Start the Frontend
cd src/frontend

python3 -m http.server 5500

Open:

http://localhost:5500
Model Evaluation

The demand forecasting model is evaluated using standard regression metrics:

Mean Absolute Error (MAE)
Mean Squared Error (MSE)
Root Mean Squared Error (RMSE)
R² Score

These metrics help measure how accurately the model predicts future product demand.

Future Improvements

Some planned enhancements include:

Multi-step time series forecasting
LSTM and Transformer-based forecasting models
Price elasticity estimation
Promotion impact analysis
Customer segmentation
Interactive analytics dashboard
PostgreSQL integration
User authentication
Docker support
Cloud deployment
What I Learned

Working on this project helped strengthen my understanding of:

Building complete machine learning pipelines
Feature engineering for time series forecasting
Demand forecasting using XGBoost
REST API development with FastAPI
Backend and frontend integration
Retail analytics and business optimization
Inventory planning and dynamic pricing strategies
Author

Pratheek Pai

Final Year Computer Science Engineering (AI & ML) Student
