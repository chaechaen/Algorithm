import java.util.*;

class Solution {
    public String solution(String number, int k) {

        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < number.length(); i++) {
            char curNum = number.charAt(i);

            while (!stack.isEmpty() && k > 0 && stack.peek() < curNum) {
                stack.pop();
                k--;
            }

            stack.push(curNum);
        }

        while (k > 0) {
            stack.pop();
            k--;
        }

        StringBuilder sb = new StringBuilder();
        for (char c : stack) {
            sb.append(c);
        }

        return sb.toString();
    }
}
