import java.util.Scanner;

public class Session_002 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        int max = 0;
        int sum = 0;

        int[] scoreArray = new int[num];

        for (int i = 0; i < scoreArray.length; i++) {
            scoreArray[i] = scanner.nextInt();
            max = max < scoreArray[i] ? scoreArray[i] : max;
            sum += scoreArray[i];
        }

        System.out.println(sum  * 100.0 / max / num);


    }
}
