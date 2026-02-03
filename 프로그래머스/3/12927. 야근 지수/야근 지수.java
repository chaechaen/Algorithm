import java.util.*;

class Solution {
public long solution(int n, int[] works) {
        long sum = 0;
        for (int w : works) sum += w;

        // 1) 야근 시간이 전체 작업량 이상이면 남는 일이 없음
        if (sum <= n) return 0;

        // 2) 최대 힙
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int w : works) pq.add(w); // works의 작업량들을 우선순위 큐에 넣음
        // -> 이제 pq.poll() 하면 현재 가장 큰 작업량을 바로 꺼낼 수 있음.

        // 3) n시간 동안 매시간 가장 큰 작업량을 1 줄이기
        while (n > 0) {
            n--;
            int max = pq.poll(); // 현재 작업량 중 가장 큰 값(최대힙이니까)을 꺼내고 큐에서 제거
            max -= 1; // 1만큼 일 함
            pq.add(max); // 그거 다시 추가
        }

        // 4) 남은 작업량 제곱합 계산
        long answer = 0;
        while (!pq.isEmpty()) {
            long x = pq.poll(); // 작업량 하나 꺼냄
            answer += x * x;
        }

        return answer;
    }
}