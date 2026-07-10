def solution(record):
    
    # 공통 코드 분리
    def parse_msg(message):
        split_msg = message.split(" ")
        command = split_msg[0]
        uid = split_msg[1]
        name = split_msg[2] if len(split_msg) > 2 else "" # leave는 이름 없음
        return command, uid, name
    
    dic = {}
    result = []
    for message in record:
        command, uid, name = parse_msg(message)
        
        if command == "Enter" or command == "Change":
            dic[uid] = name
    
    result = []
    
    for message in record: 
        command, uid, _ = parse_msg(message)
            
        if command == "Enter":
            result.append(f"{dic[uid]}님이 들어왔습니다.")
        elif command == "Leave":
            result.append(f"{dic[uid]}님이 나갔습니다.")
        
    return result