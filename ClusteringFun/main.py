import random

header = ["height(cm)", "weight(kg)"] #, "size(t-shirt)"]
X_train = [
    [158, 58], # "M"
    [158, 59], # "M"
    [158, 63], # "M"
    [160, 59], # "M"
    [160, 60], # "M"
    [163, 60], # "M"
    [163, 61], # "M"
    [160, 64], # "L"
    [163, 64], # "L"
    [165, 61], # "L"
    [165, 62], # "L"
    [165, 65], # "L"
    [168, 62], # "L"
    [168, 63], # "L"
    [168, 66], # "L"
    [170, 63], # "L"
    [170, 64], # "L"
    [170, 68] # "L"
]
# TODO: normalize data before calculating distances

# k-means clustering algorithm (a greedy algorithm)
# 1. Pick a k (e.g. k = 2)
# 2. Select k (random) instances for the initial cluster centroids (has an effect on the final resulting clusters… not guaranteed to find the "global" optimal solution, just a "local" optimal solution)
# 3. Assign each instance to the cluster with the “nearest” centroid
# 4. Re-calculate the centroids
# 5. Repeat steps #3-4 until the centroids no longer "move"

def perform_k_means_clustering(table, k):
    # how to represent clusters?
    # 1. list of instances
    # one list for each cluster
    # 2. add a column to the table for storing
    # each instances's cluster number
    # this is recommended because this is similar to how sklearn's KMeans
    # is implemented
    # and you can use groupby!!
    # https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
    table = [row.copy() + [None] for row in table]

    # step 2
    random_instances = random.sample(table, k) # without replacement
    print(random_instances)
    for i in range(len(random_instances)):
        random_instances[i][-1] = i
    for instance in table:
        print(instance)

    # step 3
    #cluster_centers = compute_cluster_centroids(table, k)
    #for instance in table:
    #     nearest_cluster_num = find_nearest_cluster(instance, cluster_centers)
    #     instance[-1] = nearest_cluster_num

    # step 4
    # new_cluster_centers = compute_cluster_centroids(table, k)

    # step 5
    # moved = check_clusters_moved(cluster_centers, new_cluster_centers)
    # while moved... repeat steps 3-4

    # goal of this function is to return two lists
    # the first is a list of labels (cluster numbers)
    # that is parallel to X_train
    # the second is a list of cluster centers (AKA centroids)
    # there are k of them
    return [], [] # TODO: fix this

# step 0
random.seed(0) # for reproducible results

# step 1
k = 2 # TODO: tune this parameter

labels_, cluster_centers_ = perform_k_means_clustering(X_train, k)
print("labels_:", labels_)
print("cluster_centers_:", cluster_centers_) # following sklearn's naming convention