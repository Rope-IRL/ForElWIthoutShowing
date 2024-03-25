import numpy as np
import matplotlib.pyplot as plt
from forEl import get_clusters



def main(r, acc):
    #here we generate numbers in 2 dimensions but, we can also make array in range from 0 to 255 and make array 28x28 like in minst
    random_points = np.random.randint(0, 20, (100, 2))
    # print(random_points)
    labels = get_clusters(random_points, r, acc)
    print(labels)
    


if __name__ == "__main__":
    #Here we need to change radius for "ok" number of clusters
    main(5, 0.001)