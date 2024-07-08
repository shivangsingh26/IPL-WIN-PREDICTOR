# IPL Win Predictor

This project is an IPL (Indian Premier League) Win Predictor that utilizes machine learning models to predict the probability of a team winning a match based on current game statistics. The project includes a machine learning model implemented in Python and an interactive web application built using Streamlit.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Files](#files)
- [Model Details](#model-details)
- [Streamlit Application](#streamlit-application)
- [Results](#results)
- [Requirements](#requirements)
- [License](#license)

## Overview
The IPL Win Predictor uses historical match data to train a logistic regression model that predicts the win probability of a batting team during a match. The web application provides an intuitive interface for users to input current match details and get real-time win probabilities.

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

4. **`streamlit run app.py`**

## Usage

  To use the web application:

1. Select the `batting` and `bowling` teams.
   
2. Select the `host` city.
   
3. Enter the `target` score.
   
4. Enter the `current score`, `overs completed`, and `wickets out`.
   
5. Click on the `Predict Probability` button to get the win probabilities for both teams.

## Files Required

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
