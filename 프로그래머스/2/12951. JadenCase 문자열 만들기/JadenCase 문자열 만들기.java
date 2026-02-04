class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        boolean isStart = true;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (c == ' ') {
                isStart = true;
            } else {
                c = isStart ? Character.toUpperCase(c) : Character.toLowerCase(c);
                isStart = false;
            }
            sb.append(c);
        }

        return sb.toString();
    }
}