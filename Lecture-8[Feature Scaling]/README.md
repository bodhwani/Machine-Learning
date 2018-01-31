# Feature Scaling

 Its a method for rescaling the features. It is used if one feature dominates the effect of other one. This will reduce the importance of other features and thus, feature scaling normalizes all the features to give equal importance.

 ```sh
X(new rescaled value) = X - Xmin/(Xmax - Xmin)

 ```

 **Disadvantage : If you have outliers in your dataset, then your Xmax - Xmin will have really extreme value**

 **Note : 
 Support Vactor machine and K means clustering are both affected by feature scaling**
