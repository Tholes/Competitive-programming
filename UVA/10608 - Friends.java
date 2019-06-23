
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    static int n = 30005;
    static List<Integer>[] grafo = new List[n];
    static boolean[] visitados = new boolean[n];

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int casos = Integer.parseInt(st.nextToken());
        for (int i = 0; i < casos; i++) {
            
            for (int j = 0; j < n; j++) {
                grafo[j] = new ArrayList<Integer>();
            }
            visitados = new boolean[n];
            
            st = new StringTokenizer(br.readLine());
            int nodos = Integer.parseInt(st.nextToken());
            int aristas = Integer.parseInt(st.nextToken());
            for (int j = 0; j < aristas; j++) {
                st = new StringTokenizer(br.readLine());
                int u = Integer.parseInt(st.nextToken());
                int v = Integer.parseInt(st.nextToken());
                grafo[u].add(v);
                grafo[v].add(u);
            }
            int amigos  = 0;
            for (int j = 1; j < nodos+1; j++) {
                if(!visitados[j]){
                    amigos = Math.max(bfs(j),amigos);
                }
            }
            System.out.println(amigos);
        }

    }

    static int bfs(int inicio) {
        Deque<Integer> cola = new LinkedList<>();
        int amigos=0;
        cola.addLast(inicio);
        while (!cola.isEmpty()) {
            int u = cola.pop();
            if (visitados[u]) {
                continue;
            }
            visitados[u] = true;
            amigos++;
            for (int i = 0; i < grafo[u].size(); i++) {
                int siguiente = grafo[u].get(i);
                if (!visitados[siguiente]) {
                    cola.add(siguiente);
                }
            }
        }
        return amigos;

    }
}