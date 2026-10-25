import java.util.*;

class Solution {
    public String solution(int[] food) {
        int cnt = food.length - 1;
        
        Deque<String> dq = new ArrayDeque<>();
        dq.add("0"); // 중앙 물 먼저 추가
        
        for(int i = food.length-1; i > 0; i--){
            int res = food[i] / 2;
            if(res != 0){
                // cnt를 문자로 바꿔 res만큼 반복시켜 덱에 추가
                String str = String.valueOf(cnt).repeat(res);
                dq.addFirst(str);
                dq.addLast(str);
                cnt--;
            } else{
                cnt--;
            }
        }
        
        StringBuilder sb = new StringBuilder();
        for(String s : dq){
            sb.append(s);
        }
        
        return sb.toString();
    }
}