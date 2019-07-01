import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(
                new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n, m;
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        while (n != 0) {
            HashMap<Integer, Integer> cd = new HashMap<Integer, Integer>();
            for (int i = 0; i < n; i++) {
                cd.put(Integer.parseInt(br.readLine()), 0);
            }
            int contador = 0;
            for (int i = 0; i < m; i++) {
                if (cd.containsKey(Integer.parseInt(br.readLine()))) {
                    contador++;
                }
            }
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            System.out.println(contador);
        }
    }