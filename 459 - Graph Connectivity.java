
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    static int n = 40;
    static List<Integer>[] grafo = new List[n];
    static boolean[] visitados = new boolean[n];

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int casos = Integer.parseInt(br.readLine());
        String conexiones;
		int nodos;
		br.readLine();
        for (int i = 0; i < casos; i++) {
            for (int j = 0; j < n; j++) {
                grafo[j] = new ArrayList<Integer>();
            }
            visitados = new boolean[n];
            nodos = (int) (br.readLine()).charAt(0) - 65;
            while ((conexiones = br.readLine()) != null) {
                if (conexiones.isEmpty()) {
                    break;
                }
                int u = (int) conexiones.charAt(0) - 65;
                int v = (int) conexiones.charAt(1) - 65;
                grafo[u].add(v);
                grafo[v].add(u);
            }
            
            int contador = 0;
            for (int j = 0; j <= nodos; j++) {
                if (!visitados[j]) {
                	
                    contador++;
                    bfs(j);
                }
            }
            if(i != casos-1){
            	System.out.println(contador);
            	System.out.println("");
            }
            else {
            	System.out.println(contador);
            }
            
        }

    }

    static void bfs(int inicio) {
        Deque<Integer> cola = new LinkedList<Integer>();
        cola.add(inicio);
        while (!cola.isEmpty()) {
            int u = cola.pop();
            if (visitados[u]) {
                continue;
            }
            visitados[u] = true;
            for (int i = 0; i < grafo[u].size(); i++) {
                int vecino = grafo[u].get(i);
                if (!visitados[vecino]) {
                    cola.add(vecino);

                }

            }

        }
    }

}