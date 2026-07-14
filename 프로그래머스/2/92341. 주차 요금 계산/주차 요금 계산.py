import math

def solution(fees, records): # 주차요금, 입출차내역
    """
    - 차량번호별로 누적 주차 시간 계산 (~23:59) => 분으로 바꾸기
    - 누적 주차 시간이 기본시간 이하라면 기본요금
    - 누적 주차 시간이 기본시간 초과라면 기본요금+((누적주차시간-기본시간)/단위시간)*단위요금
        * 초과한 시간이 나누어떨어지지 않으면 올림
    """
    
    # 시간->분 변환 후 주차시간 계산 함수
    def change_to_min(in_time, out_time): 
        in_hour, in_minute = map(int, in_time.split(":"))
        out_hour, out_minute = map(int, out_time.split(":"))
        
        return (60*out_hour+out_minute)-(60*in_hour+in_minute) # 주차시간
    
    # 주차요금 계산 함수
    # 기본시간:base_time, 기본요금:base_fee, 단위시간:unit_time, 단위요금:unit_fee
    def calc_fee(base_time, base_fee, unit_time, unit_fee, parking_time):
        if parking_time <= base_time:
            return base_fee
        else:
            return base_fee + math.ceil((parking_time - base_time) / unit_time) * unit_fee
        
    # 파싱
    base_time, base_fee, unit_time, unit_fee = fees
    
    curr_in = {}
    parking_time = {}
    
    ans = []
    
    for record in records:
        time, car, inout = record.split(" ")
        
        if inout == "IN":
            curr_in[car] = time # 해당 차량의 입차시각 저장
            if car not in parking_time:
                parking_time[car] = 0 # 처음 입차된 차량
        
        elif inout == "OUT": # 기록이 OUT이면
            in_time = curr_in[car]
            total_time = change_to_min(in_time, time) # in일 때 시각과 out일 때 시각 보내서 계산
            
            parking_time[car] += total_time # 해당 차량에 대한 누적 주차 시간 더해주기
            del curr_in[car] # 기록 삭제
                
    # 아직 출차하지 않고 남은 차량들 23:59 기준으로 정산
    for car, in_time in curr_in.items():
        total_time = change_to_min(in_time, "23:59")
        parking_time[car] += total_time
        
    for car in sorted(parking_time.keys()):
        res = calc_fee(base_time, base_fee, unit_time, unit_fee, parking_time[car])
        ans.append(res)
        
    return ans
        