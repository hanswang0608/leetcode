object Solution {
    def scoreOfString(s: String): Int = {
        var sum = 0;
        for (i <- 1 to s.length()-1) {
            sum += (s.charAt(i).toInt - s.charAt(i-1).toInt).abs
        }
        sum
    }
}