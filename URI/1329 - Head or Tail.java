import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        short partidas = Short.parseShort(st.nextToken());
        short mary=0,john=0;
        while(partidas != 0){
            st = new StringTokenizer(br.readLine());
            while(st.hasMoreElements()){
                if((Byte.parseByte(st.nextToken())) == 0){
                    mary++;
                } else {
                    john++;
                }
            }
            
            
            System.out.println("Mary won "+mary+" times and John won "+john+" times");
            mary=0;
            john = 0;
            partidas = Short.parseShort(br.readLine());
        }        
    }
}