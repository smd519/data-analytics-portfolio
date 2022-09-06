# data-analytics-portfolio

## 1. [Category Mining](https://github.com/smd519/data-analytics-portfolio/blob/main/Product_Reviews/CategoryMining.ipynb)
In this project, we analyze a product-reviews dataset from the Amazon Kindle Store(e-books).Our hypothesis is that users interested in a certain type of book (e.g., books about sports) tend to rate and review similar books. We test this hypothesis, by running a spectral co-clustering of a user-product graph to see how books cluster.
+ The clustering code comes from the [scikit-learn](https://scikit-learn.org/stable/) package. 
+ We prepare the data and process the results.
## 2. [Taxi Trip Analysis; Finding The Shortest Path](https://github.com/smd519/data-analytics-portfolio/blob/main/TaxiTripAnalysis/TaxiData.md)
In this project, we analyze the Yellow Taxi Trip Data from NYC Taxi dataset. Our hypothesis is that  there are cheaper or faster alternative routes than direct path between two zones. We test this hypothesis, by calculating the travel time for each trip, and visualizing the distributions of distance, time, and cost. Then, We setup a graph using NetworkX graph representation, and perform graph queries for the shortest path.

+ The networkx code comes from the [from_scipy_sparse_matrix package](https://networkx.org/documentation/stable/reference/generated/networkx.convert_matrix.from_scipy_sparse_matrix.html).
+ We prepare the data and process the results.

## 3. [Credit Default Prediction](https://github.com/smd519/data-analytics-portfolio/blob/main/Credit_Default_Prediction/Credit_Default_Prediction.ipynb)
In this project, we use consumer credit card profile data to predict if a consumer will default in the future. Dataset includes 190 features which are are anonymized and normalized and includes only the following categaries: spend, payment, balance, risk, and delinquency features. Our hypothesis is that Balance variables will be more important in predicting default than the others, i.e. Customers with higher balances are more likely to default. We test this hypothesis, by running Principal Component Analysis, Lasso Regression and Logistic Regression. We have utilized SQLite, R and Python.

## 4. [Handwritten Digit Classification](https://github.com/smd519/data-analytics-portfolio/blob/main/Handwritten_Digit_Classification/code_Handwritten_Digit_Classification.ipynb)
In this project, we evaluate the behavior and performance of 3 supervised clas-sification algorithms for classifying the handwritten digits. The dataset provided includes normalized handwritten digits, scanned from envelopes by the U.S. Postal Service. Pre-processing and feature extraction techniques are already applied on the original scanned images with different sizes and orientations (Le Cun et al., 1990). Each image is represented by a la-bel-id 0-9 (V1), and a vector of 256 grayscale values (V2-V257). The code is in R.
