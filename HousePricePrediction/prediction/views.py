from django.shortcuts import render 
import pandas as pd #  Pandas is a Python library used mainly for data manipulation and analysis.
import matplotlib.pyplot as plt 
import seaborn as sns # Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.
import numpy as np # NumPy and Pandas are two popular Python libraries often used in data analytics 
from sklearn.model_selection import train_test_split # sklearn is a python library to implement machine learning models and statistical modelling
from sklearn.linear_model import LinearRegression # it is used for prediction of machine learning models
from sklearn import metrics
from  .models import *
from django.contrib.auth import logout


def home(request): 
	return render(request, 'home.html') 

def predict(request): 
	return render(request, 'predict.html') 

def about(request): 
	return render(request, 'about.html')

def login_success(request): 
	return render(request, 'login_failure.html') 

def login_failure(request): 
	return render(request, 'login_success.html') 

def logoutPage(request): 
      logout(request,Details)
      return render(request, 'logout.html') 



def result(request): 
	data = pd.read_csv(r"USA_housing.csv") #This line reads a CSV file named "USA_housing.csv" into a pandas DataFrame named 
	data = data.drop(['Address'], axis=1) #This line removes the 'Address' column from the data DataFrame.
	X = data.drop('Price', axis=1) #Here, X contains all the columns except 'Price', which are the features for prediction. Y contains the 'Price' column, which is the target variable we want to predict.
	Y = data['Price'] #Y contains the 'Price' column, which is the target variable we want to predict.
	X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size= .30) #This line splits the data into training and testing sets, with 70% of the data used for training and 30% for testing.

	model = LinearRegression() #A linear regression model is instantiated and then trained using the training data (X_train and Y_train).
	model.fit(X_train, Y_train) 

	var1 = float(request.GET['n1']) #These lines extract five input variables from the HTTP GET request and convert them to floats. The variables n1 through n5 are assumed to be the names of the parameters passed in the request.
	var2 = float(request.GET['n2']) 
	var3 = float(request.GET['n3']) 
	var4 = float(request.GET['n4']) 
	var5 = float(request.GET['n5']) 
	

	pred = model.predict(np.array([var1, var2, var3, var4, var5]).reshape(1, -1)) #The input variables are put into a NumPy array, reshaped to match the (expected input shape for the model,) and then used to make a prediction with the trained model.

	pred = round(pred[0])#The prediction is rounded to the nearest integer. Since model.predict returns an array, pred[0] is used to get the first (and only) element of the array. '''

	price = "The Predicted Rent Is Rs "+str(pred) #This line creates a string that includes the rounded prediction value.
	return render(request, 'predict.html', {"result2":price})



def register(request):
    if(request.method=="POST"):
        Fullname = request.POST.get('Fullname')
        Username = request.POST.get('Username')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        DOB = request.POST.get('DOB')
        Gender = request.POST.get('Gender')
        Language = request.POST.get('Language')
        Aadhar = request.POST.get('Aadhar')
        Profilepic = request.POST.get('Profilepic')
        data = Details(Name=Fullname, Username=Username, Email=Email, Password=Password, DOB=DOB, Gender=Gender,Language=Language, Aadhar=Aadhar, Profilepic=Profilepic )
        data.save()
        return render(request,"login.html")   
    return render(request,"register.html",)


def login(request):
    return render(request, 'login.html')
    
def login(request):
    if(request.method == "POST"):
        T1 = request.POST.get('T1')
        T2 = request.POST.get('T2')
        S1 = Details.objects.all().values_list()
        temp  = 0
        for i in S1:
            if i[2] == T1 and i[4] ==   T2:
                return render(request, 'login_success.html')
                temp += 1
                break
        if temp == 0:
            return render(request, 'login_failure.html')
   
    else:
        return render(request, 'login.html')
    

