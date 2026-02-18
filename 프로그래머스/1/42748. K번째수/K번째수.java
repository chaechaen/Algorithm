import java.util.*;

class Solution {
    
    public int[] solution(int[] array, int[][] commands) {
        
        int[] answer = new int[commands.length];
        
        for (int idx = 0; idx < commands.length; idx++) {
            
            int i = commands[idx][0];
            int j = commands[idx][1];
            int k = commands[idx][2];
            
            ArrayList<Integer> arr = new ArrayList<>();
            
            for (int s = i - 1; s <= j - 1; s++) {
                arr.add(array[s]);
            }
            
            Collections.sort(arr);
            
            answer[idx] = arr.get(k - 1);
        }
        
        return answer;
    }
}
