import collections 
import heapq

def topKFrequent(words, k):
    count = collections.Counter(words)
    heap = [(freq, word) for word, freq in count.items()]
    heapq.heapify(heap)
    answer = [heapq.heappop(heap)[1] for _ in range(k)]   
    answer.reverse() 
    return answer 

words = ["i", "love", "leetcode", "i", "love", "coding"]
frequency = 3
result = topKFrequent(words, frequency);
print(result)