
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Deque;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {

    static int n = 205;
    static HashMap<String, ArrayList<String>> grafo = new HashMap<String, ArrayList<String>>();
    static LinkedList<String> palabras = new LinkedList<>();
    static HashMap<String, Integer> visitado = new HashMap<>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int casos = Integer.parseInt(st.nextToken());
        br.readLine();
        String palabra;
        for (int i = 0; i < casos; i++) {
            
            while (!(palabra = br.readLine()).equals("*")) {
                palabras.add(palabra);
                grafo.put(palabra, new ArrayList<String>());
            }

            Iterator<String> indice = palabras.iterator();
            while (indice.hasNext()) {
                palabra = indice.next();
                Iterator<String> indiceAux = palabras.iterator();
                while (indiceAux.hasNext()) {
                    String auxiliar = indiceAux.next();
                    if (auxiliar.length() == palabra.length()) {
                        int dif = 0;
                        for (int j = 0; j < auxiliar.length(); j++) {
                            if (auxiliar.charAt(j) != palabra.charAt(j)) {
                                dif++;
                            }
                        }
                        if (dif == 1) {
                            grafo.get(palabra).add(auxiliar);
                            grafo.get(auxiliar).add(palabra);
                        }
                    }
                }

            }

            String auxiliar;
            while ((auxiliar = br.readLine()) != null) {
                if (auxiliar.isEmpty()) {
                    break;
                }
                st = new StringTokenizer(auxiliar);
                String inicio = st.nextToken();
                String fin = st.nextToken();
                visitado.clear();
                bfs(inicio);
                System.out.println(inicio + " " + fin + " " + (visitado.get(fin) + 1));
            }
            if(i != casos -1){
                System.out.println("");
            }
            grafo.clear();
            palabras.clear();

        }
    }

    static void bfs(String inicio) {
        Deque<String> cola = new LinkedList<>();
        cola.add(inicio);
        Iterator<String> indice = palabras.iterator();
        while (indice.hasNext()) {
            visitado.put(indice.next(), -1);
        }

        while (!cola.isEmpty()) {
            String u = cola.pop();
            for (int i = 0; i < grafo.get(u).size(); i++) {
                String vecino = grafo.get(u).get(i);
                if (visitado.get(vecino) == -1) {
                    cola.add(vecino);
                    visitado.put(vecino, visitado.get(u) + 1);
                }
            }
        }
    }
}