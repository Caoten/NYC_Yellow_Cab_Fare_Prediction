from sklearn.cluster import KMeans
import numpy as np
import pandas as pd

def KMeans_Binning(df,num_cluster):
    kmeans=KMeans(n_clusters=num_cluster,random_state=1)
    kmeans_assignment=kmeans.fit(df["Fare_Amt"].values.reshape(-1,1))
    df["Fare_Rate_K_Means"]=kmeans_assignment.labels_
    return df

# (min,6]=1,(6,8]=2,(8,11]=3,(11,14]=4,(14,19]=5,(19,24]=6,(24,30]=7,(30,38]=8,(38,47]=9,(47,61]=10,(61,122]=11
def own_binning_target(df,min,max):
    bins=[min,6,8,11,14,19,24,30,38,47,61,max]
    labels=[1,2,3,4,5,6,7,8,9,10,11]
    target=df["Fare_Amt"].to_numpy().flatten()
    df['Fare_Rate'] = pd.cut(target,bins=bins,labels=labels)
    # Drop Columns
    df.drop(columns=["Fare_Amt","Fare_Rate_K_Means"],inplace=True)
    return df

