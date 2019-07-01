
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int n = 10005;
    static List<Integer>[] grafo = new List[n];
    static boolean[] visitados = new boolean[n];
    static int caen;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int casos = Integer.parseInt(st.nextToken());
        while (casos-- > 0) {
            caen = 0;
            for (int i = 0; i < n; i++) {
                grafo[i] = new ArrayList<Integer>();
            }
            
            st = new StringTokenizer(br.readLine());
            int nodos = Integer.parseInt(st.nextToken());
            int aristas = Integer.parseInt(st.nextToken());
            int tumbar = Integer.parseInt(st.nextToken());
            for (int i = 0; i < aristas; i++) {
                st = new StringTokenizer(br.readLine());
                int u = Integer.parseInt(st.nextToken());
                int v = Integer.parseInt(st.nextToken());
                grafo[u].add(v);
            }
            for (int i = 0; i < tumbar; i++) {          
                int inicio = Integer.parseInt(br.readLine());
                if(!visitados[inicio]){
                    dfs(inicio);
                }                   
            }
            System.out.println(caen);
            visitados = new boolean[n];
        }
    }
    static void dfs(int inicio){
        visitados[inicio] = true;
        caen++;
        for (int i = 0; i < grafo[inicio].size(); i++) {
            int siguiente = grafo[inicio].get(i);
            if(!visitados[siguiente]){
                dfs(siguiente);           
            }
        }
    }
}