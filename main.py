import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder, MinMaxScaler
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

# 1. Load Data
print("--- Data Loading ---")
df = pd.read_csv('diabetes_prediction_dataset.csv')
print(df.head())

# 2. Data Exploration
print("\n--- Data Exploration ---")
df.info()
print("\nDescribe:\n", df.describe())
print("\nNull Values:\n", df.isnull().sum())
print("\nDuplicated sum before:", df.duplicated().sum())

# Cleaning
df.drop_duplicates(inplace=True)
print("Duplicated sum after:", df.duplicated().sum())

print("\nTarget (Diabetes) counts:\n", df['diabetes'].value_counts())
print("\nHypertension counts:\n", df['hypertension'].value_counts())
print("\nHeart Disease counts:\n", df['heart_disease'].value_counts())

# Gender Cleaning
print("\nGender unique values before:", df['gender'].unique())
df['gender'].replace('Other', np.nan, inplace=True)
df['gender'].fillna(df['gender'].mode()[0], inplace=True)
print("Gender unique values after:", df['gender'].unique())

print("\nSmoking History unique values:", df['smoking_history'].unique())

# 3. Data Visualization (Saving instead of Showing)
print("\n--- Generating Visualizations ---")

plt.figure(figsize=(6,4))
sns.countplot(x='gender', data=df, palette='Blues')
plt.title('Gender Distribution')
plt.savefig('gender_distribution.png')
plt.close()

plt.figure(figsize=(6,4))
sns.countplot(x='smoking_history', data=df, palette='Blues')
plt.xlabel('Smoking History')
plt.savefig('smoking_history.png')
plt.close()

plt.figure(figsize=(6,4))
sns.countplot(x='hypertension', data=df, palette='Blues')
plt.xlabel('Hypertension')
plt.savefig('hypertension.png')
plt.close()

plt.figure(figsize=(6,4))
sns.countplot(x='diabetes', data=df, palette='Blues')
plt.title("Diabetes Distribution")
plt.savefig('diabetes_distribution.png')
plt.close()

plt.figure(figsize=(10,6))
sns.histplot(df['age'], kde=True, palette='Blues')
plt.title('Age Distribution')
plt.savefig('age_distribution.png')
plt.close()

plt.figure(figsize=(8, 6))
sns.boxplot(x='diabetes', y='age', data=df, palette='Blues')
plt.title('Age Distribution by Diabetes Status')
plt.xlabel('Diabetes (0: No, 1: Yes)')
plt.ylabel('Age')
plt.savefig('age_boxplot.png')
plt.close()

plt.figure(figsize=(10,6))
sns.heatmap(df[["hypertension", "heart_disease", "diabetes"]].corr(), annot=True)
plt.savefig('heatmap.png')
plt.close()

print("All 7 images saved successfully.")

# 4. Preprocessing
print("\n--- Preprocessing ---")
df = pd.get_dummies(df, columns=['smoking_history'], drop_first=True) 
df = df.replace({True: 1, False: 0})

# Encoding
le = LabelEncoder()
df['gender'] = le.fit_transform(df['gender'])

# Scaling
numeric_columns = ['age', 'bmi', 'HbA1c_level', 'blood_glucose_level']
scale = MinMaxScaler()
df[numeric_columns] = scale.fit_transform(df[numeric_columns])

print("\nFinal Data Info after Preprocessing:")
df.info()
print("\nSample of processed data:\n", df.head())
print("\n--- Project Execution Finished ---")