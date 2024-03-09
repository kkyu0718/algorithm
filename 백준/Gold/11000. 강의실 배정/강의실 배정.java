import java.io.*;
import java.util.*;
import java.util.regex.Pattern;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException{
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int[][] arr = new int[n][2];

        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> {
            return o1[1] - o2[1];
        });

        for(int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());

            arr[i][0] = n1;
            arr[i][1] = n2;
        }

        Arrays.sort(arr, (o1, o2) -> {
            return o1[0] - o2[0];
        });

        for(int i = 0; i < n; i++) {
            int start = arr[i][0];
            int end = arr[i][1];

            if(!pq.isEmpty() && pq.peek()[1] <= start) {
                pq.poll();
                pq.add(new int[]{start, end});
            } else {
                pq.add(new int[]{start, end});
            }
        }
        System.out.println(pq.size());
    }
}
