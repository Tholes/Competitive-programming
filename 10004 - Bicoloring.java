
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    static int n = 205;
    static List<Integer>[] grafo = new List[n];
    static int[] pintas = new int[n];
    static boolean visitados[] = new boolean[n];

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int nodos;

        while ((nodos = Integer.parseInt(st.nextToken())) != 0) {

            for (int j = 0; j < n; j++) {
                grafo[j] = new ArrayList<Integer>();
            }
            pintas = new int[n];
            visitados = new boolean[n];
            int aritas = Integer.parseInt(br.readLine());
            for (int i = 0; i < aritas; i++) {
                st = new StringTokenizer(br.readLine());
                int u = Integer.parseInt(st.nextToken());
                int v = Integer.parseInt(st.nextToken());
                grafo[u].add(v);
                grafo[v].add(u);
            }
            if (bfs(0)) {
                System.out.println("BICOLORABLE.");
            } else {
                System.out.println("NOT BICOLORABLE.");
            }
            st = new StringTokenizer(br.readLine());
        }

    }

    static boolean bfs(int inicio) {
        Deque<Integer> cola = new LinkedList<Integer>();
        cola.add(inicio);
        pintas[inicio] = 1;
        visitados[inicio] = true;
        while (!cola.isEmpty()) {
            int u = cola.pop();
            for (int i = 0; i < grafo[u].size(); i++) {
                int vecino = grafo[u].get(i);
                if (!visitados[vecino]) {
                    cola.add(vecino);
                    pintas[vecino] = pintas[u] * (-1);
                    visitados[vecino] = true;
                    cola.add(vecino);

                } else if (pintas[vecino] == pintas[u]) {
                    return false;
                }

            }

        }
        return true;
    }

}