class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = []
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        hitsWithin5min = 0
        for hit in self.hits:
            if hit > timestamp - 300 and hit <= timestamp:
                hitsWithin5min += 1
        
        return hitsWithin5min

counter = HitCounter()

counter.hit(1)

# counter.getHits(1)

counter.hit(2);

counter.hit(3);

# counter.getHits(4);

counter.hit(300);

# counter.getHits(300);

counter.getHits(301); 



