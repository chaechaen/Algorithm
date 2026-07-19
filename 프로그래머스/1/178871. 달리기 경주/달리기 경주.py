def solution(players, callings):
    
    player_idx = {player: i for i, player in enumerate(players)} # player_idx = {이름: 인덱스}
    
    for name in callings:
        curr_idx = player_idx[name] # 해당 이름의 players에서의 인덱스
        front_name = players[curr_idx - 1]
        
        players[curr_idx - 1], players[curr_idx] = players[curr_idx], players[curr_idx - 1]
        
        player_idx[name] = curr_idx - 1
        player_idx[front_name] = curr_idx
    
    return players