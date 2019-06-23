import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    static int n = 10005;
    static List<Integer>[] grafo = new List[n];
    static boolean[] visitados = new boolean[n];
    static int[] dist = new int[n];

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            grafo[i] = new ArrayList<Integer>();
        }

        int nodos = Integer.parseInt(st.nextToken());

        for (int i = 0; i < nodos - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            grafo[u].add(v);
            grafo[v].add(u);
        }

        int indice = bfs(1);
        int distancia = dist[indice];
        dist = new int[n];
        visitados = new boolean[n];
        indice = bfs(indice);
        distancia = Math.max(distancia, dist[indice]);
        System.out.println(distancia);
    }

    static int bfs(int inicio) {
        Deque<Integer> cola = new LinkedList<Integer>();
        cola.add(inicio);
        int indice = 0, distancia = 0;
        while (!cola.isEmpty()) {
            int u = cola.pop();
            if (visitados[u]) {
                continue;
            }
            visitados[u] = true;
            for (int i = 0; i < grafo[u].size(); i++) {
                int vecino = grafo[u].get(i);
                if (!visitados[vecino]) {
                    dist[vecino] = dist[u] + 1;
                    cola.add(grafo[u].get(i));
                    if (dist[vecino] > distancia) {
                        distancia = dist[vecino];
                        indice = vecino;
                    }

                }

            }

        }
        return indice;
    }

}