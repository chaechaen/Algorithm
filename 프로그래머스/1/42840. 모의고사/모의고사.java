import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        
        
        int[] s1 = {1,2,3,4,5};
        int[] s2 = {2,1,2,3,2,4,2,5};
        int[] s3 = {3,3,1,1,2,2,4,4,5,5}; // 각 학생의 찍는 패턴
        
        int[] scores = {0,0,0}; // 배열 초기화
        
        for (int i = 0; i < answers.length; i++){
            if (answers[i] == s1[i % (s1.length)]) { // 패턴 반복
                scores[0]++;
            }
            if (answers[i] == s2[i % (s2.length)]) {
                scores[1]++;
            }
            if (answers[i] == s3[i % (s3.length)]) {
                scores[2]++;
            }
        }
        
        int maxScore = scores[0];
        for (int j = 1; j < scores.length; j++) {
            if (scores[j] > maxScore) { // 가장 점수 높은 학생
                maxScore = scores[j];
            }
        }
        
        ArrayList<Integer> list = new ArrayList<>();
        for (int i = 0; i < scores.length; i++) {
            if (scores[i] == maxScore) {
                list.add(i + 1);
            }
        }

        int[] answer = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }
        
        return answer;
    }
}