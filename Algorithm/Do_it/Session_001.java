import java.util.Scanner;

public class Session_001 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        String strNum = sc.next();
        char[] numArray = strNum.toCharArray();

        int sum = 0;

        for (int i = 0; i < numArray.length; i++) {
            sum += numArray[i] - '0';
        }

        System.out.println(sum);
    }
}
