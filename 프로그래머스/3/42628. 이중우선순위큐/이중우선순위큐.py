import heapq

def solution(operations):
    queue = []

    for o in operations:
        if o.startswith("I"):
            i, num = o.split(" ")
            heapq.heappush(queue, int(num))

        if o == "D -1":
            if queue:
                heapq.heappop(queue)

        if o == "D 1":
            if queue:
                large = heapq.nlargest(1, queue) # 최댓값 뽑고
                queue.remove(large[0]) # 그걸 리스트에서 삭제 후
                heapq.heapify(queue) # 다시 힙으로 만들기

    # 최종 큐에서 최솟값과 최댓값 가져와서 리스트로 만들어 반환.
    if queue:
        return [heapq.nlargest(1, queue)[0], heapq.nsmallest(1, queue)[0]]
    else:
        return [0, 0]