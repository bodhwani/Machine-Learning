# Support Vector Machine (SVM):
In simple terms, it is an algorithm, which takes data as an input, and output line, that seperates the two classes(given as inputs).
So we classify the data correctly and subject to that constraints, we maximize the margin.

For understanding code, refer to <a href="http://scikit-learn.org/stable/modules/svm.html">Sklearn Documentation</a>

<br>
There are basically two types of SVMs:
- Linear SVM
- Non-linear SVM



### Parameters in SVC :

- Kernel Trick :
There are functions, that take low dimensional input space or feature space and map it to very high dimensional space. So they convert non linear seperable problem into seperable problem. These fucntions are called Kernels.


- Gamma parameter :
It defines how far the influence of a single training example reaches.
High value of gamma, give weightage to those values, which are closer to the decision boundary.
On the other hand, low value of gamma, focuses on the points, which are far away from the decision boundary.

- C parameter :
It controls tradeoff between smooth decision boundary and classifying training points correctly. Large value of C, gives more training points correctly.

### Comparing Naive Bayes and SVM :
As we have seen before, Naive Bayes has(if you had run nb_author_id.py) : <br>
- training time: 2.98 s
- prediction time: 0.223 s
- accuracy; 0.97326507394766781
<br>
Whereas, on the other hand, SVM has :<br>
- training time: 212.841 s
- prediction time: 22.491 s
- accuracy, 0.98407281001137659

So, SVM is much slower as compared to Naive Bayes.
To fast SVM algorithm, we can reduce training data. 
Refer to the <a href="https://github.com/bodhwani/Machine-Learning/blob/master/_Solutions/svm/svm_author_id.py">code</a> to know, how to reduce training data.<br>
After reducing, accuracy comes out to be :
- accuracy: 0.88452787258248011
- training time: 0.141 s
- training time: 1.25 s
Pretty Good!

**Note** 
- On changing kernel from linear to rbf, we get 
Accuracy: 0.61604095563139927
Not good at all!

- If we increase the value of C, then accuracy comes out to be :
0.89249146757679176
Bingo!

**Therefore, if we are reducing the training set and apply kernel as rbf, then we must have high value of C, to get high accuracy**