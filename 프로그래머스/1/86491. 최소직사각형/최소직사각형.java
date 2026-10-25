import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        
        for(int[] s : sizes){
            Arrays.sort(s);
            int temp = s[0];
            s[0] = s[1];
            s[1] = temp; // 내림차순으로
        }
        
        ArrayList<Integer> first_lst = new ArrayList<>();
        ArrayList<Integer> last_lst = new ArrayList<>();
        
        for(int[] item : sizes) {
            first_lst.add(item[0]);
            last_lst.add(item[1]);
        }
        
        return Collections.max(first_lst) *  Collections.max(last_lst);
    }
}