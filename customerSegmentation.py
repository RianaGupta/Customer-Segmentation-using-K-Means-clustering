import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df=pd.read_csv("Mall_Customers.csv")
print(df.head())

X = df[["Annual Income (k$)", "Spending Score (1-100)"]]

wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()

kmeans = KMeans(n_clusters=5, random_state=42)
y_kmeans = kmeans.fit_predict(X)

plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=y_kmeans)
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.show()