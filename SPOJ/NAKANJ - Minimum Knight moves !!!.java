
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

public class Main {

    static HashMap<Character, Integer> letras = new HashMap<>();
    static int[] x = {-1, 1, 2, 2, 1, -1, -2, -2};
    static int[] y = {-2, -2, -1, 1, 2, 2, 1, -1};

    public static void main(String[] args) throws IOException { 
        BufferedReader br = new BufferedReader( new InputStreamReader(System.in));
        PrintWriter out= new PrintWriter(System.out);
        letras.put('a', 1);
        letras.put('b', 2);
        letras.put('c', 3);
        letras.put('d', 4);
        letras.put('e', 5);
        letras.put('f', 6);
        letras.put('g', 7);
        letras.put('h', 8);
        
        int casos = Integer.parseInt(br.readLine());
        while (casos-- > 0) {
            
            String[] inicio = br.readLine().split(" ");
            out.println(bfs(inicio[0],inicio[1]));
        }
        out.close();
    }

    public static int bfs(String inicio, String fin) {
        int[][] tablero = new int[9][9];
        boolean[][] visitados = new boolean[9][9];
        int y1 = Integer.parseInt("" + inicio.charAt(1));
        int x1 = letras.get(inicio.charAt(0));
        int y2 = Integer.parseInt("" + fin.charAt(1));
        int x2 = letras.get(fin.charAt(0));
        Queue<Integer> colaX = new LinkedList<Integer>();
        Queue<Integer> colaY = new LinkedList<Integer>();
        colaX.add(x1); colaY.add(y1);
        while (!colaX.isEmpty()) {
            x1 = colaX.poll(); y1 = colaY.poll();
            
            if(x1 == x2 && y1 == y2){
                return tablero[x2][y2];
            }
            if (visitados[x1][y1]) {
                continue;
            }           
            
            visitados[x1][y1] = true;
            for (int i = 0; i < 8; i++) {
                int auX = x1 + x[i];
                int auY = y1 + y[i];
                if (auX < 1 || auX > 8 || auY < 1 || auY > 8) {
                    continue;
                }
                if (!visitados[auX][auY]) {
                    colaX.add(auX); colaY.add(auY);                  
                    tablero[auX][auY] = tablero[x1][y1] + 1;
                    //System.out.println(tablero[auX][auY]+" : "+auX+" "+auY);
                }

            }

        }
        return tablero[x2][y2];
    }
}
   
    