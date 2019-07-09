
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st = new StringTokenizer("");
    static PrintWriter out = new PrintWriter(System.out);
    static int n = 31;
    static char[][][] mapa = new char[n][n][n];
    static int inX, inY, inZ;

    public static void main(String[] args) throws IOException {
        int r, l, c;
        while ((l = nextInt()) != 0 && (r = nextInt()) != 0 && (c = nextInt()) != 0) {
            for (int i = 0; i < l; i++) {
                for (int j = 0; j < r; j++) {
                    String aux = next();
                    int z = aux.indexOf("S");
                    if (z >= 0) {
                        inX = z;
                        inY = j;
                        inZ = i;
                    }
                    mapa[i][j] = aux.toCharArray();
                }
            }

            out.println(bfs(l, r, c));

            mapa = new char[n][n][n];

        }
        out.close();
    }

    static String bfs(int l, int r, int c) {
        int[] z = {1, 0, -1, 0, 0, 0};
        int[] y = {0, 1, 0, -1, 0, 0};
        int[] x = {0, 0, 0, 0, 1, -1};
        int[][][] dist = new int[n][n][n];
        boolean[][][] visitados = new boolean[n][n][n];
        Queue<Tupla> cola = new LinkedList<Tupla>();
        cola.add(new Tupla(inZ, inY, inX));

        while (!cola.isEmpty()) {
            Tupla aux = cola.poll();
            int x1 = aux.x;
            int y1 = aux.y;
            int z1 = aux.z;
            if (visitados[z1][y1][x1]) {
                continue;
            }

            if (mapa[z1][y1][x1] == 'E') {
                return ("Escaped in " + dist[z1][y1][x1] + " minute(s).");
            }

            visitados[z1][y1][x1] = true;

            for (int i = 0; i < 6; i++) {
                int auX = x1 + x[i];
                int auY = y1 + y[i];
                int auZ = z1 + z[i];
                if (auX < 0 || auX >= c || auY < 0 || auY >= r || auZ < 0 || auZ >= l) {
                    continue;
                }
                //out.println(mapa[auZ][auY][auX] + " : " + auZ + " " + auY + " " + auX);
                if (mapa[auZ][auY][auX] != '#') {
                    dist[auZ][auY][auX] = dist[z1][y1][x1] + 1;
                    cola.add(new Tupla(auZ, auY, auX));
                }
            }

        }

        return "Trapped!";
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
}

class Tupla {

    int x, y, z;

    public Tupla(int z, int y, int x) {
        this.x = x;
        this.y = y;
        this.z = z;
    }
}