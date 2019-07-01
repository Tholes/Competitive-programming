
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    
    static BufferedReader br= new BufferedReader(new InputStreamReader(System.in)); ;
    static StringTokenizer st = new StringTokenizer("");
    static int n = 100005;
    static List<Integer>[] grafo = new List[n];
    static boolean[] visitados = new boolean[n];
    static Stack<Integer> pila = new Stack<>();
    public static void main(String[] args) throws IOException {
        int casos = nextInt();
        while(casos-- >0){
            for (int i = 0; i < n; i++) {
                grafo[i] = new ArrayList<Integer>();
            }
            
            int nodos = nextInt();
            int aristas = nextInt();
            for (int i = 0; i < aristas; i++) {
                int u = nextInt();
                int v = nextInt();
                grafo[u].add(v);
            }
            for (int i = 1; i <= nodos; i++) {
                if(!visitados[i]){
                    dfs(i);
                }
            }
            int count= 0;
            visitados = new boolean[n];
            while(!pila.isEmpty()){
                int u = pila.pop();
                if(!visitados[u]){
                    count++;
                    dfs(u);
                }
            }
            System.out.println(count);
            visitados = new boolean[n];
        }
        
    }
    static String next() throws IOException {
        while (!st.hasMoreTokens()) {
            st = new StringTokenizer(br.readLine());
        }
        return st.nextToken();
    }

    static int nextInt() throws IOException {
        return Integer.parseInt(next());
    }
    static void dfs(int inicio){
        visitados[inicio] = true;
        for (int i = 0; i < grafo[inicio].size(); i++) {
            int siguiente = grafo[inicio].get(i);
            if(!visitados[siguiente]){
                dfs(siguiente);
            }
        }
        pila.add(inicio);
    }
}