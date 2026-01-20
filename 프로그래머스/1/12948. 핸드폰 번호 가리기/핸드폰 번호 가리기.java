class Solution {
    public String solution(String phone_number) {
        int len = phone_number.length();

        String last = phone_number.substring(len - 4);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < phone_number.length() - 4; i++) {
            sb.append("*");
        }

        return sb.toString() + last;
    }
}