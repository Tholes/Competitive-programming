
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(
                new InputStreamReader(System.in));
        short n = Short.parseShort(br.readLine());
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int[] casas = new int[Integer.parseInt(st.nextToken())];
            int mayor = 0;

            for (int j = 0; j < casas.length; j++) {
                casas[j] = Integer.parseInt(st.nextToken());
            }

            int suma = 0;
            int menor = Integer.MAX_VALUE;
            for (int j = 0; j < casas.length; j++) {
                for (int k = 0; k < casas.length ; k++) {
                    suma += Math.abs(casas[j] - casas[k]);
                }
                menor = Math.min(suma, menor);
                suma = 0;
            }
            System.out.println(menor);
        }
    }
}