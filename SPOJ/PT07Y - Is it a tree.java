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
    static boolean ans = false;
    public static void main(String[] args) throws Exception {
       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
       StringTokenizer st = new StringTokenizer(br.readLine());
       int nodos, aristas;
        for (int i = 0; i < n; i++) {
            grafo[i] = new LinkedList<Integer>();
        }
        nodos = Integer.parseInt(st.nextToken());
        aristas = Integer.parseInt(st.nextToken());
        for (int i = 0; i < aristas; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            grafo[u].add(v);
            grafo[v].add(u);
        }
        int contador = 0;
        for (int i = 1; i < nodos+1; i++) {
            if(!visitados[i]){
                contador++;
                dfs(i);
            }            
        }
       if(contador == 1 && !ans){
           System.out.println("YES");
       }
       else{
           System.out.println("NO");
       }
                  
    }
    
    static void dfs(int fuente){
        visitados[fuente] = true;
        for (int i = 0; i < grafo[fuente].size(); i++) {
            int siguiente = grafo[fuente].get(i);
            if(!visitados[siguiente]){
                dfs(siguiente);
            }
            else if(siguiente != grafo[fuente].get(0)){
                ans = true;
            }
        }
    }
}