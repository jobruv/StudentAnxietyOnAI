import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Dataset credit goes to Sridip Basu on Kaggle
#https://www.kaggle.com/datasets/sridipbasu/ai-depndency-career-anxiety-and-student-burnout/code

df=pd.read_csv("ai_dependency_career_anxiety_students.csv")
print("===AI Dependency, Career Anxiety and Student Burnout===")
print("              Exploratory Data Analysis")
print("Number of rows & columns: ", df.shape)
print("--------------------------------------------")
print(df.dtypes)
print("--------------------------------------------")
print(df.head())
print("--------------------------------------------")
print(df.tail())
print("--------------------------------------------")
print(df.describe())
print("--------------------------------------------")
print(df.isnull().sum())
print(df.isnull().sum().sum(), "total nulls")
print("--------------------------------------------")
print(df.nunique())