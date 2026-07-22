import heapq

def solution(book_time):
    
    def convert_time(time): # ["15:00", "17:00"]
        start_hour, start_min = time[0].split(":")
        start = int(start_hour) * 60 + int(start_min)
        
        end_hour, end_min = time[1].split(":")
        end = int(end_hour) * 60 + int(end_min) + 10 # 청소시간 포함
        
        return start, end
    
    times = []
    for time in book_time:
        times.append(convert_time(time))
    
    times.sort() # 입실 시각 기준 정렬
    
    rooms = [] # 각 방의 청소 완료 시각
    
    for start, end in times:
        if rooms and rooms[0] <= start: # 가장 빨리 비는 방의 시각보다 현재 입실 시각이 같거나 늦으면
            heapq.heappop(rooms)
            
        heapq.heappush(rooms, end) # 새로운 손님의 청소 완료 시각 등록
        
    return len(rooms)