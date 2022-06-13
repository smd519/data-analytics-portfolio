# Introduction
In this project, we analyze a product-reviews dataset from the Amazon Kindle Store(e-books).Our hypothesis is that users interested in a certain type of book (e.g., books about sports) tend to rate and review similar books. 
We test this hypothesis, by running a _spectral co-clustering_ of a user-product graph to see how books cluster.

# Data
We are working with two dataset in this project. Both dataset are from dataset from the Amazon Kindle Store(e-books).
*The data originated with Julian McAuley [here](http://jmcauley.ucsd.edu/data/amazon/)*

## 1. Reviews dataset ###

The most relevant keys are the following:

* `'reviewerID'`: An ID string for the user who wrote the review.
* `'asin'`: An ID string for the e-book that the user reviewed.
* `'overall'`: The reviewer's rating of the e-book, on a scale of 1.0 (hated the book) to 5.0 (loved the book).
* `'reviewText'`: The reviewer's comments about the book, a string of arbitrary length.
* `'helpful'`: A two-element list. The first element is the number of other users who marked this review as being "helpful"; the second element is the number of users who looked at the review. For example, a value of `[4, 7]` means that 7 users read the review, but only 4 marked it as "helpful."


## 2. The second dataset is the metadata for e-books ###

We only need two pieces of information: 

* `'book ID'`: An ID string for the e-book that is available on Amazon Kindle Store.
* `'category'`: A list contaning the categories the product belongs to. We are interested in element 2 of the `'category'` value which represent **genre** of the e-books.
