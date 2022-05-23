import java.util.Scanner;

public class Session_005 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int num1 = sc.nextInt();
        int num2 = sc.nextInt();

        long count = 0;

        long[] sumArray = new long[num1];
        long[] array = new long[num2];

        // 구간 합 배열
        sumArray[0] = sc.nextInt();
        for (int i = 1; i < num1; i++) {
            sumArray[i] = sumArray[i - 1] + sc.nextInt();
        }

        // 나머지로 인덱스 카운팅
        for (int i = 0; i < num1; i++) {
            int remainder = (int) (sumArray[i] % num2);
            if (remainder == 0) {
                count++;
            }
            array[remainder]++;
        }

        // 나머지가 같은 인덱스 중 2개를 뽑는 경우
        for (int i = 0; i < num2; i++) {
            if (array[i] > 1) {
                count = count + (array[i] * (array[i] - 1)) / 2;
            }
        }

        System.out.println(count);
    }
}
