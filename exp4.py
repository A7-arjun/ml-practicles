
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Step 1: Create dataset
X = np.array([
    [1.713, 1.586],
    [0.180, 1.786],
    [0.353, 1.240],
    [0.940, 1.566],
    [1.486, 0.759],
    [1.266, 1.106],
    [1.540, 0.419],
    [0.459, 1.799],
    [0.773, 0.186]
])

# Step 2: Actual class labels
y = np.array([0, 1, 1, 0, 1, 0, 1, 1, 1])

# Step 3: New data point
new = np.array([[0.906, 0.606]])

# Step 4: Apply K-Means clustering
model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
).fit(X)

# Step 5: Find cluster of new point
cluster = model.predict(new)[0]

# Step 6: Find majority class in that cluster
members = y[model.labels_ == cluster]
pred = np.bincount(members).argmax()

# Step 7: Display results
print("Centres:\n", model.cluster_centers_)
print("Predicted CLASS:", pred)

# Step 8: Visualize clusters
plt.scatter(X[:, 0], X[:, 1], c=model.labels_)

plt.scatter(
    model.cluster_centers_[:, 0],
    model.cluster_centers_[:, 1],
    color="red",
    marker="X",
    s=150,
    label="Centres"
)

plt.scatter(
    new[:, 0],
    new[:, 1],
    color="blue",
    marker="s",
    s=100,
    label="New point"
)

plt.xlabel("VAR1")
plt.ylabel("VAR2")
plt.legend()
plt.show()
