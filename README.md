# IPL Win Predictor

The IPL Win Predictor is a machine learning model that predicts the probability of a team winning an Indian Premier League (IPL) match based on current match statistics. This project includes a logistic regression model implemented in Python and an interactive web application built with Streamlit, as well as containerized deployment on AWS ECR and SageMaker.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Deployment](#deployment)
- [Usage](#usage)
- [Files](#files)
- [Model Details](#model-details)
- [Streamlit Application](#streamlit-application)
- [Results](#results)
- [Requirements](#requirements)
- [License](#license)

## Overview
The IPL Win Predictor leverages historical match data to train a logistic regression model that provides real-time win probabilities based on the current state of the game. The model can be accessed through a Streamlit web app, allowing users to interactively input match details and receive win predictions.

## Installation
To run this project locally, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/shivangsingh26/IPL-WIN-PREDICTOR.git
   cd IPL-WIN-PREDICTOR
   ```
2. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```
3. **Download the dataset:**
   
   - Place `matches.csv` and `deliveries.csv` in the data directory.

   - The dataset can be found [here](https://www.kaggle.com/datasets/ramjidoolla/ipl-data-set).

4. **Run the app locally or use run the docker container from AWS ECR:**
   ```
   `streamlit run app.py`
   ```

## Deployment

This project is deployed using Docker containers on AWS ECR and AWS SageMaker.

### Docker Image Creation and Deployment to AWS ECR

1. Build Docker Image:
   ```
   docker build -t registry_ipl_win_pred .
   ```
   
2. Push Image to AWS ECR:
   
   Make sure your ECR repository is set up (e.g., registry_ipl_win_pred), then push your Docker image:

   ```
   docker tag registry_ipl_win_pred:latest 992382843941.dkr.ecr.us-east-1.amazonaws.com/registry_ipl_win_pred:latest
   docker push 992382843941.dkr.ecr.us-east-1.amazonaws.com/registry_ipl_win_pred:latest
   ```

### Deploying on AWS SageMaker

1. Create a SageMaker Notebook Instance and open a terminal.
   
2. Execute Deployment Code in the notebook to pull the Docker image from ECR and deploy it using a SageMaker model and    endpoint.

3. Access Endpoint: Once the deployment is successful, the endpoint can be accessed for predictions.

## Usage

  To use the web application:

1. Select the `batting` and `bowling` teams.
   
2. Select the `host` city.
   
3. Enter the `target` score.
   
4. Enter the `current score`, `overs completed`, and `wickets out`.
   
5. Click on the `Predict Probability` button to get the win probabilities for both teams.

## Files

- **`notebook.ipynb`**: Jupyter notebook containing the data analysis and model training code.

- **`app.py`**: Streamlit app script for the interactive web interface.

- **`data/matches.csv`**: Historical match data.

- **`data/deliveries.csv`**: Ball-by-ball delivery data.

## Model Details

The model training includes:

  - Loading and merging `match` and `delivery` data.
  - Feature engineering to create useful features like `current_score`, `runs_left`, `balls_left`, `wickets`, etc.
  - Using `logistic regression` to predict the win probability.

The main steps in the notebook.ipynb include:

  1. `Loading` and `preprocessing data`.
  2. `Feature engineering`.
  3. `Model training and evaluation`.
  4. `Saving the trained model using pickle`.

## Streamlit Application

- The `app.py` script loads the trained model and provides an interactive UI for users to input match details and get win probabilities. 
- The application is built using `Streamlit`, a powerful framework for creating web applications in `Python.`

## Results

- The model predicts win probabilities based on the current state of the match. 
- The `Streamlit` app displays the win probabilities for both the batting and bowling teams.

## Requirements

- `streamlit`
  
- `pandas`
  
- `numpy`
  
- `scikit-learn`

- `matplotlib`

## License

- This project is licensed under the MIT License. See the LICENSE file for more details.

