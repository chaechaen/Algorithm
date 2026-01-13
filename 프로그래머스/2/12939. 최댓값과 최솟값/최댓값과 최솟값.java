import java.util.*;

class Solution {
    public String solution(String s) {
         
        // 공백을 없애고 숫자로 변환
        String[] arr = s.split(" ");
        
        ArrayList<Integer> numArr = new ArrayList<>();
        
        for(String numStr : arr){
            int n = Integer.parseInt(numStr);
            numArr.add(n);
        }
        
        int maxNum = numArr.get(0);
        for (int i = 1; i < numArr.size();i++) {
            if (numArr.get(i) > maxNum) maxNum = numArr.get(i);
        }
        
        int minNum = numArr.get(0);
        for (int i = 1; i < numArr.size(); i++) {
            if (numArr.get(i) < minNum) minNum = numArr.get(i);
        }
        
        return minNum + " " + maxNum;
    }
}