
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws Exception {
       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
       StringTokenizer token = new StringTokenizer(br.readLine());
       int rutas = Integer.parseInt(token.nextToken());
       int Serval = Integer.parseInt(token.nextToken());
       int candidatoTiempo = Integer.MAX_VALUE;
       int candidatoRuta = 0;
       int[] tiempos = new int[rutas];
        for (int i = 0; i <rutas; i++) {
            token = new StringTokenizer(br.readLine());
            int primerBus = Integer.parseInt(token.nextToken());
            int intervalo = Integer.parseInt(token.nextToken());
            while(primerBus < Serval){
                primerBus += intervalo;
            }
            tiempos[i] = primerBus;
            
        }
        for (int i = 0; i < rutas; i++) {
            if(tiempos[i]<candidatoTiempo){
                candidatoTiempo = tiempos[i];
                candidatoRuta = i+1;
            }
        }
        System.out.println(candidatoRuta);
    }
}