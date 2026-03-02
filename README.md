# Customer-Segmentation-using-K-Means-clustering
This project analyzes customer data to group similar customers together. By looking at buying income and spend, it helps businesses understand their customers better.
It performs customer segmentation using the K-Means clustering algorithm. The goal is to group customers based on their Annual Income and Spending Score. This can help businesses understand customer behavior and target the right products to each group.

# Dataset
The dataset used is Mall_Customers.csv with the following columns:
CustomerID: Unique ID for each customer
Gender: Male or Female
Age: Age of the customer
Annual Income (k$): Income of the customer in thousands of dollars
Spending Score (1-100): Score assigned by the mall based on customer behavior

# Libraries Used
pandas – for data handling
numpy – for numerical operations
matplotlib – for visualization
scikit-learn – for K-Means clustering


## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the code: `python customerSegmentation.py`

### Plots

**Elbow Method Plot:**  
![Elbow Method](elbow_method.png)

**Customer Segments Plot:**  
![Customer Segments](customer_segments.png)
