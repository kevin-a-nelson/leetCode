# On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. Each worker and bike is a 2D coordinate on this grid.

# Our goal is to assign a bike to each worker. Among the available bikes and workers, we choose the (worker, bike) pair with the shortest Manhattan distance between each other, and assign the bike to that worker. (If there are multiple (worker, bike) pairs with the same shortest Manhattan distance, we choose the pair with the smallest worker index; if there are multiple ways to do that, we choose the pair with the smallest bike index). We repeat this process until there are no available workers.

# The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.

# Return a vector ans of length N, where ans[i] is the index (0-indexed) of the bike that the i-th worker is assigned to.



# N Workers
# M Bikes

# N Workers <= M Bikes

# Output: Array of length N where Array[i] is the index of the bike that the i-th worker is assigned to

# [Worker1, Worker2, Worker3][Bike]

# workerBikeDistances = []

# for workers, workerY in grid1:
#   workerBikeDistance = {}
#   for worker, workerX in workers:
#       for bikes, bikeY in grid2:
#           for bike, bikeX in bikes:
#               Manhattan distance = | workerX - bikeX | + | workerY - bikeY 


class Solution:
    def assignBikes(self, workers, bikes):
        workerBikeDistances = []
        takenBikes = []
        for workerY, workersRow in enumerate(workers):
            minDistance = float("inf")
            workerBikeDistance = {}
            for workerX, worker in enumerate(workersRow):
                for bikeY, bikesRow in enumerate(bikes):
                    for bikeX, bike in enumerate(bikesRow):

                        manhattenDistance = abs(workerX - bikeX) + abs(workerY - bikeY)

                        if(manhattenDistance < minDistance):
                            workerBikeDistance['workerIdx'] = workerX
                            workerBikeDistance['bikeIdx'] = bikeX
                            workerBikeDistance['manhattenDistance'] = manhattenDistance


            workerBikeDistances.append(workerBikeDistance)
            print(workerBikeDistance)
            # takenBikes.append(workerBikeDistance['bikeIdx'])
        return workerBikeDistances



solution = Solution()

workers = [[0,0],[2,1]] 
bikes = [[1,2],[3,3]]

solution.assignBikes(workers, bikes)