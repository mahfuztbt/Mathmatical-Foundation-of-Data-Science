
import pandas as pd
import json
import copy

#get all the intersection points of the path, select the point closest to the target location
def getKeyPoint(routes1, routes2, pt1, pt2):
    all_inters = getAllInters(routes1,routes2)
    min_distance = 99999999
    key_pt = []
    for inter in all_inters:
        routes1 = getAllRoutes(inter,pt1)
        routes2 = getAllRoutes(inter,pt2)
        distance = len(routes1[0]) + len(routes2[0])
        if distance < min_distance:
            key_pt = inter
            min_distance = distance
    return key_pt
    
#get the possible intersection of the two shortest paths
def getAllInters(routes1,routes2):
    all_inters = []
    for route1 in routes1:
        for route2 in routes2:
            for i in range(1,len(route1)):
                if route1[i] in route2:
                    all_inters.append(route1[i])
    return all_inters

# solve all the ways according to the directed chain
def getAllRoutes(from_id, to_id):
    print(from_id, to_id)
    front_neighbors = getAllFrontNeighbor(from_id, to_id)
    print(front_neighbors)
    routes = []
    reversed_routes = [[to_id]]
    temp_reversed_routes = []
    i = 0
    while True:
        get_end = False
        temp_reversed_routes = []
        for route in reversed_routes:
            for front_pt in front_neighbors[route[-1]-1]:
                temp_reversed_routes.append(route+[front_pt])
                if front_pt == from_id:
                    get_end = True
        reversed_routes = copy.deepcopy(temp_reversed_routes)
        if get_end == True:
            break
        i = i +1 
    for item in reversed_routes:
        item.reverse()
        routes.append(item)
    # print(routes)
    return routes

# Get all one-way network
def getAllFrontNeighbor(from_id,to_id):
    cur_pts = [from_id] # the point outside the current round
    searched_pts = [from_id] # locations that have been retrieved
    around_graph = [] # graphs stored by distance
    cur_distance = 1 # Current distance
    front_neighbors = [[] for i in range(problem.shape[0])] #there may be multiple adjacent edges in front

    while True:
        # First calculate all the surrounding points
        all_neighbor_pts = []
        for cur_pt in cur_pts:
            for pt_id in neighbors[cur_pt-1]:
                if pt_id not in searched_pts:
                    if pt_id not in all_neighbor_pts:
                        all_neighbor_pts.append(pt_id)
                    front_neighbors[pt_id-1].append(cur_pt)
        # After calculating the area of the round
        around_graph.append(all_neighbor_pts)
        cur_pts = all_neighbor_pts
        searched_pts = searched_pts + all_neighbor_pts

        if to_id in searched_pts:
            break

    return front_neighbors

if __name__ == "__main__":
    problem_id = 3
    problem = pd.read_csv("data/problem" + str(problem_id) + "_graph.csv")
    neighbors = []

    for i in range(problem.shape[0]):
        neighbors.append(json.loads(problem["neighbor"][i]))

    from_id, to_id1 = 1, 13 # Starting position and target position
    routes1 = getAllRoutes(from_id,to_id1) # Get all the paths
    print("all path from 1-13: ")
    print(routes1)
    
    from_id, to_id2 = 1, 9 # Starting position and target position
    routes2 = getAllRoutes(from_id,to_id2) # Get all the paths
    print("all path from 1-19: ")
    print(routes2)

    key_pt = getKeyPoint(routes1,routes2,to_id1,to_id2)
    print("The starting point to the end point and the potential decision-making position of the mine: ")
    print(key_pt)
