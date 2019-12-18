from sklearn.cluster import KMeans
import numpy as np
import pandas as pd

def KMeans_Binning(df,num_cluster):
    kmeans=KMeans(n_clusters=num_cluster,random_state=1)
    kmeans_assignment=kmeans.fit(df["Fare_Amt"].values.reshape(-1,1))
    df["Fare_Rate"]=kmeans_assignment.labels_
    return df



