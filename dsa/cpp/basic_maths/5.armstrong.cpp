class Solution {
public:
    bool isArmstrong(int n) {
        int original = n;
        int sum = 0;

        // count digits
        int digits = to_string(n).length();

        while(n > 0) {
            int d = n % 10;
            sum += pow(d, digits);
            n /= 10;
        }

        return sum == original;
    }
};