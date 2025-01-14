
# Linear Regression for Binance Coin (BNB) Price Prediction

This project implements a linear regression model to predict Binance Coin (BNB) daily closing prices using historical data from Yahoo Finance. It includes training the model on 2022 data and predicting prices for the first quarter of 2023.

## Features

- **Data Acquisition**: Uses `yfinance` to download historical daily closing prices for BNB.
- **Linear Regression Model**: Implements matrix-based linear regression.
- **Model Evaluation**: Calculates Mean Squared Error (MSE) for both the training set (2022) and test set (2023).
- **Visualization**: Plots actual vs. predicted prices for both 2022 and 2023.

## Requirements

- Python 3.7+
- Libraries:
  - `yfinance`
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `scikit-learn`

Install dependencies using:
```bash
pip install yfinance scikit-learn matplotlib pandas numpy
```

## File Overview

- **LinearRegressionBNBPrice.ipynb**: Jupyter Notebook containing the code for:
  - Data fetching and preprocessing.
  - Model training using 2022 data.
  - Predictions for 2023 prices.
  - Visualization of results.

## Usage

1. **Run the Notebook**: Execute the cells sequentially to:
   - Download historical BNB prices.
   - Train the model using 2022 data.
   - Evaluate the model and generate predictions for 2023.
2. **Visualize Results**: Examine the plots showing:
   - Actual vs. predicted prices for 2022.
   - Predictions for the first quarter of 2023.
   - Overlay of real and predicted prices for 2023.

## Outputs

- **Error Metrics**: Mean Squared Error (MSE) for both training and test sets.
- **Plots**:
  - Daily closing prices for 2022 with predictions.
  - Predicted vs. actual prices for Q1 2023.

## License

This project is open-source and available under the [MIT License](https://opensource.org/license/MIT).
