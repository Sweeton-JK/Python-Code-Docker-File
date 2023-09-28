# kmeans.py
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

np.random.seed(0)
X = np.random.rand(100, 2)

num_clusters = 3

kmeans = KMeans(n_clusters=num_clusters)

kmeans.fit(X)

labels = kmeans.labels_

centroids = kmeans.cluster_centers_

for i in range(num_clusters):
    plt.scatter(X[labels == i, 0], X[labels == i, 1], label=f'Cluster {i + 1}')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=200, linewidths=3, color='black', label='Centroids')
plt.legend()
plt.title('K-Means Clustering')
plt.show()
