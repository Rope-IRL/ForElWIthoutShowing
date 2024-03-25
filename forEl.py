import numpy as np

def get_clusters(points, radius, acc = 0.01):
    center_points = []
    
    while len(points) != 0:
        #here we choose random point and get it's neighbors
        cur_point = get_random_point(points)
        neighbors = get_neighbors(cur_point, radius, points)
        center_point = get_center_point(neighbors)
        #change data untill range beetween points will be higher than accuracy
        #maybe can change to some const number
        while np.linalg.norm(cur_point - center_point) > acc:
            cur_point = center_point
            neighbors = get_neighbors(cur_point, radius, points)
            center_point = get_center_point(neighbors)

        points = remove_points(neighbors, points)
        center_points.append(cur_point)
    return center_points     

# get point neighbors obv, which lies in circle
def get_neighbors(cur_point, radius, points):
    neighbors = [point for point in points if np.linalg.norm(cur_point - point) < radius]
    return np.array(neighbors)

def get_center_point(points):
    #print(points)
    pts = []
# going in np array collumns and chosing avg point like: sum(point.value)/number of points
    for i in range(len(points[0])):
        pts.append(np.mean(points[:,i]))
    return np.array(pts)

def get_random_point(points):
    rnd_index = np.random.choice(len(points), 1)[0]
    return points[rnd_index]

#removing points that lies in circle, means that points will be in that cluster
def remove_points(sub_points,pointis):
    points = [point for point in pointis if point not in sub_points]
    return points