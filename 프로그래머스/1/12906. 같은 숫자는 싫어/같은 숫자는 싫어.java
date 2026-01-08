import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        
        List<Integer> result = new ArrayList<>();
        
        for (int cur : arr) {
            if (result.isEmpty()){ // 비었으면 무조건 넣기
                result.add(cur);
            } else {
                int last = result.get(result.size() - 1);
                if (last != cur) {
                    result.add(cur);
                }
            }
        }

        int[] answer = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            answer[i] = result.get(i);
        }
        
        return answer;
    }
}