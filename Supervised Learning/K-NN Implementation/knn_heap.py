from heap import Heap

import numpy as np
import pandas as pd


def euclidean_distance(point_a, point_b):
    distance = np.linalg.norm(point_a - point_b)
    return distance

#Complexity of the knn_heap algorithm: O( (n^2)*log(k) )
def k_nn_heap(X_test, X_train, Y_train, k):
  y_hat=[]
  
  X_test_numpy=X_test.to_numpy();
  X_train_numpy=X_train.to_numpy();
  Y_train_numpy=Y_train.to_numpy();

  for cr in X_test_numpy:
    cnt=[0, 0]
    h=Heap();

    for i in range(0, k):
      h.insert( (euclidean_distance(X_train_numpy[i], cr), i) );

    for i in range(k, len(X_train_numpy) ):
      h.erase_root();
      h.insert( (euclidean_distance(X_train_numpy[i], cr), i)  );


    for i in range(k):
      cnt[Y_train_numpy[ h.get_max()[1] ] ]+=1;
      h.erase_root();
    
    if cnt[0]>cnt[1]:
      y_hat.append(0)
    else:
      y_hat.append(1)
   
  
  return y_hat






