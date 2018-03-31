# Feature Selection
You should be haivng minimum number of features to capture the patterns in your data.
**Two things can be done**
- Select best feature
- Add new feature

**Note - Features and information are two different things.** 
Quality of features is the information. So,
**You should have minimum number of features, which gives maximum no of information**

### Bias-Variance Dilemma and No of features
- High bias - pays little attention to data oversimplified - higher error on training set
- pays too much attention to data(does not generalize well) - overfits - much higher error on test set than on training set.

### Regularization
A method of selecting feature that gives maximum output. It does the job of - **Features and information are two different things.** 
In other words, it automatically penalizing extra Features
<br>
Suppose you have y = m1x1 + m2x2 + m3x3 + m4x4 + b
If x3,x4 doesnt play important role in variane of data, then m3 and m4 will be set to 0.

