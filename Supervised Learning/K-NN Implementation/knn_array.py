import numpy as np
import pandas as pd


def euclidean_distance(point_a, point_b):
    distance = np.linalg.norm(point_a - point_b)
    return distance


#Complexity of the knn_array algorithm: O( (n^2)log(n) )
def knn_array(X_test, X_train, Y_train, k):
  y_hat=[]
  
  #print(len(X_test.to_numpy() ) );
  #cnttt=0;

  X_test_numpy=X_test.to_numpy();
  X_train_numpy=X_train.to_numpy();
  Y_train_numpy=Y_train.to_numpy();

  for cr in X_test_numpy:
    #cnttt+=1;
    #print(cnttt);
    cnt=[0, 0]

    arr=[]

    for i in range(0, len(X_train_numpy)):
      arr.append( ( euclidean_distance(X_train_numpy[i], cr) , i ) );

    arr.sort();
    for i in range(0, k):
        cnt[Y_train_numpy[ arr[i][1] ] ]+=1;
    
    if cnt[0]>cnt[1]:
      y_hat.append(0)
    else:
      y_hat.append(1)
   

  return y_hat