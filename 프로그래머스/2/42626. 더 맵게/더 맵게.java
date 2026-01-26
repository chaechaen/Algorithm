import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        
        PriorityQueue<Long> pq = new PriorityQueue<>();

        for (int s : scoville) { 
            pq.add((long) s); // scoville 안의 값들을 우선순위 큐에 넣음
        }

        int count = 0;

        while (pq.peek() < K) { // 가장 작은 값이 K보다 작으면 아직 모두가 K보다 크지 x
            if (pq.size() == 1) return -1;
            pq.add(pq.poll() + pq.poll() * 2);
            count++;
        }   

        return count;
    }
}