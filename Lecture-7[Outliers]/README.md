# Outliers 

Outliers are defined as the collection of points, which are very much seperated from regression line, in regression.

So in machine learning, we try to ignore the outliers because they often caused by sensor malfunctioning and when you over-fit them, you really get bad results.

In case of fraud detection, people pay attention to remove outliers(called as freak events). So these will prove as advatage to them.

**So depending on your application, you might hate them, or might love them.**


### Outliers detection and Rejection:
- Train
- Remove ~10% data which is giving highly residual error(called as outlier).
- Train Again
- Repeat steps 1,2,3(if required)


For example, given figure has highest residual error :

![alt text](../screenshots/residualError.png, "Highest residual error")


**What we'll do is fit the regression on all training points discard the 10% of points that have the largest errors between the actual y values, and the regression-predicted y values refit on the remaining points**



Note : In cleaning process, we always clean on training data, not on testing data.

- Before cleaning :
This is the slope with training data 5.07793064
<br>
This is the score with testing data 0.878262470366

- After cleaning :
This is the slope with training data 6.36859481
<br>
This is the score with testing data 0.983189455396

### Identifying and cleaning away outliers is something you should always think about when looking at a dataset for the first time.

Refer to the <a href="https://github.com/bodhwani/Machine-Learning/tree/master/_Solutions/outliers">code</a>, for calculating slope and score, before and after removing outliers.



