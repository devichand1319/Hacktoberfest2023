import random
import math

def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def total_distance(route, points):
    distance = 0
    for i in range(len(route) - 1):
        distance += euclidean_distance(points[route[i]], points[route[i + 1]])
    distance += euclidean_distance(points[route[-1]], points[route[0]])
    return distance

def simulated_annealing(points, initial_temperature, cooling_rate, iterations):
    n = len(points)
    current_route = list(range(n))
    current_distance = total_distance(current_route, points)
    best_route = current_route
    best_distance = current_distance

    for iteration in range(iterations):
        temperature = initial_temperature * (1 - iteration / iterations)
        random.shuffle(current_route)
        new_distance = total_distance(current_route, points)

        if new_distance < current_distance or random.random() < math.exp((current_distance - new_distance) / temperature):
            current_distance = new_distance
            if new_distance < best_distance:
                best_route = current_route
                best_distance = new_distance

    return best_route, best_distance

if __name__ == "__main__":
    # Define a set of points (coordinates)
    points = [(0, 0), (1, 2), (2, 4), (3, 1), (4, 3)]

    # Parameters for Simulated Annealing
    initial_temperature = 100.0
    cooling_rate = 0.99
    iterations = 10000

    # Find the best route and its distance
    best_route, best_distance = simulated_annealing(points, initial_temperature, cooling_rate, iterations)

    print("Best Route:", best_route)
    print("Best Distance:", best
