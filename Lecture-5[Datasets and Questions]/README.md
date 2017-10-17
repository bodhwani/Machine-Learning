# Datasets and Questions :

It is quite obvious thing to note, that 
**The more data we have, the better accuracy we will get**, from the applied algorithm.

We will be working on Enron Dataset. You can download dataset from <a href="https://www.cs.cmu.edu/~./enron/">here</a>

### Types of Data :
- Numerical - example : Salary information
- Categorical - example : Men or woman, or how many stars you give for rating a movie.
- Time series - temporal value(date+timestamp) - example : finance
- Text - words, to/from fields from emails.

A python dictionary can’t be read directly into an sklearn classification or regression algorithm; instead, it needs a numpy array or a list of lists

Again, difference between features and labels(to brush up your concepts):
<br>
Briefly, feature is input; label is output.
<br>
A feature is one column of the data in your input set. For instance, if you're trying to predict the type of pet someone will choose, your input features might include age, home region, family income, etc. The label is the final choice, such as dog, fish, iguana, rock, etc.
<br>
Once you've trained your model, you will give it sets of new input containing those features; it will return the predicted "label" (pet type) for that person.

**Note:**
I’ve written some helper functions (featureFormat() and targetFeatureSplit() in tools/feature_format.py) that can take a list of feature names and the data dictionary, and return a numpy array.

*This lecture mainly deals with dataset and extracting values from dictionary. So, I would suggest to go through <a href="https://github.com/bodhwani/Machine-Learning/tree/master/_Solutions/datasets_questions">code</a>, and get your hands dirty*