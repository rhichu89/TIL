import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Session_004 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int num = Integer.parseInt(st.nextToken());
        int qNum = Integer.parseInt(st.nextToken());

        int[][] arr = new int[num+1][num+1];

        for (int i = 1; i <= num; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= num; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int[][] sumArr = new int[num + 1][num + 1];

        for (int i = 1; i <= num; i++) {
            for (int j = 1; j <= num; j++) {
                sumArr[i][j] = sumArr[i][j - 1] + sumArr[i - 1][j] - sumArr[i - 1][j - 1] + arr[i][j];
            }
        }

        for (int i = 0; i < qNum; i++) {
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());

            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());

            int result = sumArr[x2][y2] - sumArr[x1-1][y2] - sumArr[x2][y1-1] + sumArr[x1-1][y1-1];
            System.out.println(result);
        }

    }
}
