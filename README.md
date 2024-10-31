# data-analytics-portfolio

## 1. [Flight Delay Prediction Dashboard](https://github.com/smd519/data-analytics-portfolio/tree/main/Flight_Delay_Prediction_Dashboard)
'On-Time Aviation' is a machine learning based flight delay prediction dashboard," an innovative project that aims to develop an interactive dashboard to accurately predict flight delays for common routes.
+ The UI implementation: We used [D3](https://d3js.org/) to develop an html page containing all the UI elements including US map, capability to select source and destination on the MAP, curved line with arrowhead to show the flight between two airports, filters to choose date and airline, and tables to show the results.
+ Algorithm: A self paced ensemble with XGBoost was selected due to its efficacy in evaluating imbalanced and noisy datasets.
  
## 2. [Category Mining](https://github.com/smd519/data-analytics-portfolio/blob/main/Product_Reviews/CategoryMining.ipynb)
In this project, we analyze a product-reviews dataset from the Amazon Kindle Store(e-books).Our hypothesis is that users interested in a certain type of book (e.g., books about sports) tend to rate and review similar books. We test this hypothesis, by running a spectral co-clustering of a user-product graph to see how books cluster.
+ The clustering code comes from the [scikit-learn](https://scikit-learn.org/stable/) package. 
+ We prepare the data and process the results.
  
## 3. [Taxi Trip Analysis; Finding The Shortest Path](https://github.com/smd519/data-analytics-portfolio/blob/main/TaxiTripAnalysis/TaxiData.md)
In this project, we analyze the Yellow Taxi Trip Data from NYC Taxi dataset. Our hypothesis is that  there are cheaper or faster alternative routes than direct path between two zones. We test this hypothesis, by calculating the travel time for each trip, and visualizing the distributions of distance, time, and cost. Then, We setup a graph using NetworkX graph representation, and perform graph queries for the shortest path.
+ The networkx code comes from the [from_scipy_sparse_matrix package](https://networkx.org/documentation/stable/reference/generated/networkx.convert_matrix.from_scipy_sparse_matrix.html).
+ We prepare the data and process the results.

## 4. [Credit Default Prediction](https://github.com/smd519/data-analytics-portfolio/blob/main/Credit_Default_Prediction/Credit_Default_Prediction.ipynb)
In this project, we use consumer credit card profile data to predict if a consumer will default in the future. Dataset includes 190 features which are are anonymized and normalized and includes only the following categaries: spend, payment, balance, risk, and delinquency features. Our hypothesis is that Balance variables will be more important in predicting default than the others, i.e. Customers with higher balances are more likely to default. We test this hypothesis, by running Principal Component Analysis, Lasso Regression and Logistic Regression. We have utilized SQLite, R and Python.

## 5. [Handwritten Digit Classification](https://github.com/smd519/data-analytics-portfolio/blob/main/Handwritten_Digit_Classification/code_Handwritten_Digit_Classification.ipynb)
In this project, we evaluate the behavior and performance of 3 supervised clas-sification algorithms for classifying the handwritten digits. The dataset provided includes normalized handwritten digits, scanned from envelopes by the U.S. Postal Service. Pre-processing and feature extraction techniques are already applied on the original scanned images with different sizes and orientations (Le Cun et al., 1990). Each image is represented by a la-bel-id 0-9 (V1), and a vector of 256 grayscale values (V2-V257). The code is in R.

## 6. [Estimation of Body Fat Based on Body Circumference Measurments](https://github.com/smd519/data-analytics-portfolio/tree/main/Estimatation_Percentage_Body_Fat) 
In this project, we evaluate the behavior and performance of several linear regression algorithms for estimating the body fat based on other body measurements. We utulize LASSO, RIDGE, stepwise, best subset of features, Principal component, and Partial least squares regression. The dataset provided includes age, weight, height, percent body fat using Siri’s equation, Density, Adiposity index, Fat Free Weight and circumference of chest, neck, abdomen, hip, thigh, knee, ankle, biceps, fore-arm, and wrist(Johnson R. 1996). The code is in R.

## 7. [Prediction of Fuel Efficiency for Vehicles](https://github.com/smd519/data-analytics-portfolio/blob/main/Prediction_Fuel_Efficiency_Vehicles/Prediction_Fuel_Efficiency_Vehicles.pdf) 
In this project, we evaluate the behavior and performance of several classification methods for classifying the city-cycle fuel efficency in miles per gallon based on other specification of a car. We evaluate [linear discriminant analysis (LDA)](https://en.wikipedia.org/wiki/Linear_discriminant_analysis), [quadratic discriminant analy-sis (QDA)](https://en.wikipedia.org/wiki/Quadratic_classifier#Quadratic_discriminant_analysis), [naive bayes regression](https://en.wikipedia.org/wiki/Naive_Bayes_classifier), logistic regression, and k-nearest neighbor. The code is in R.
