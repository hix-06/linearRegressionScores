import pandas as pd
import matplotlib.pyplot as plt  
from sklearn.model_selection import train_test_split  
from sklearn.linear_model import LinearRegression  
from sklearn import metrics  

url = "http://bit.ly/w-data"
s_data = pd.read_csv(url)
print("Data imported successfully")
print(s_data.head(5))


s_data.plot(x='Hours', y='Scores', style='o')  
plt.title('Hours vs Percentage')  
plt.xlabel('Hours Studied')  
plt.ylabel('Percentage Score')  
plt.show()

X = s_data.iloc[:, :-1].values  
y = s_data.iloc[:, 1].values  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 

regressor = LinearRegression()  
regressor.fit(X_train, y_train) 
print("Training complete.")

line = regressor.coef_*X+regressor.intercept_
plt.scatter(X, y)
plt.plot(X, line);
plt.show()

y_pred = regressor.predict(X_test)

df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})  
print(df) 

hours = 11
own_pred = regressor.predict([[hours]])
# Limit the predicted score to be no more than 100
predicted_score = min(own_pred[0], 100)
print("No of Hours = {}".format(hours))
print("Predicted Score = {}".format(predicted_score))

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))

r_squared = regressor.score(X_test, y_test)
print('R-squared:', r_squared)


# What I have learned in this internship task
print("\nWhat I've Learned:")
print("- How to import and explore a dataset using pandas.")
print("- Creating informative visualizations using matplotlib.")
print("- Preparing data for machine learning, splitting it into training and testing sets.")
print("- Building and training a Linear Regression model using scikit-learn.")
print("- Evaluating the model's performance with metrics like Mean Absolute Error and R-squared.")
print("- Making predictions on new data points.")
print("- evaluate model using MAE and R-squared")
