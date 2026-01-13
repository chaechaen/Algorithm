class Solution {
    boolean solution(String s) {
        boolean answer = true;
        
        int[] count = {0,0};
        
        String upperS = s.toUpperCase();
        for (char c : upperS.toCharArray()) {
            if (c == 'P') {
                count[0]++;
            } else if (c == 'Y'){
                count[1]++;
            }
        }
        
        if (count[0]==count[1]) {
            answer = true;
        }
        
        else{
            answer = false;
        }

        return answer;
    }
}