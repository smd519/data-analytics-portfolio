# data-analytics-portfolio

## 1. [Category Mining](https://github.com/smd519/data-analytics-portfolio/blob/main/Product_Reviews/CategoryMining.ipynb)
In this project, we analyze a product-reviews dataset from the Amazon Kindle Store(e-books).Our hypothesis is that users interested in a certain type of book (e.g., books about sports) tend to rate and review similar books. We test this hypothesis, by running a spectral co-clustering of a user-product graph to see how books cluster.
+ The clustering code comes from the [scikit-learn](https://scikit-learn.org/stable/) package. 
+ We prepare the data and process the results.
## 2. [Taxi Trip Analysis; Finding The Shortest Path](https://github.com/smd519/data-analytics-portfolio/blob/main/TaxiTripAnalysis/TaxiData.md)
In this project, we analyze the Yellow Taxi Trip Data from NYC Taxi dataset. Our hypothesis is that  there are cheaper or faster alternative routes than direct path between two zones. We test this hypothesis, by calculating the travel time for each trip, and visualizing the distributions of distance, time, and cost. Then, We setup a graph using NetworkX graph representation, and perform graph queries for the shortest path.

+ The networkx code comes from the [from_scipy_sparse_matrix package](https://networkx.org/documentation/stable/reference/generated/networkx.convert_matrix.from_scipy_sparse_matrix.html).
+ We prepare the data and process the results.
