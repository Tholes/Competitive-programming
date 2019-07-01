
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws Exception {
       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
       HashMap <Character,String> valor = new HashMap<>();
       valor.put('A', "2");
       valor.put('B', "2");
       valor.put('C', "2");
       valor.put('D', "3");
       valor.put('E', "3");
       valor.put('F', "3");
       valor.put('G', "4");
       valor.put('H', "4");
       valor.put('I', "4");
       valor.put('J', "5");
       valor.put('K', "5");
       valor.put('L', "5");
       valor.put('M', "6");
       valor.put('N', "6");
       valor.put('O', "6");
       valor.put('P', "7");
       valor.put('Q', "7");
       valor.put('R', "7");
       valor.put('S', "7");
       valor.put('T', "8");
       valor.put('U', "8");
       valor.put('V', "8");
       valor.put('W', "9");
       valor.put('X', "9");
       valor.put('Y', "9");
       valor.put('Z', "9");
       valor.put('1', "1");
       valor.put('2', "2");
       valor.put('3', "3");
       valor.put('4', "4");
       valor.put('5', "5");
       valor.put('6', "6");
       valor.put('7', "7");
       valor.put('8', "8");
       valor.put('9', "9");
       valor.put('0', "0");
       
       
       
       
       String frase ="";
       while((frase = br.readLine()) != null){
           frase = frase.trim();
           String nueva = "";
           for (int i = 0; i < frase.length(); i++) {
               if (frase.charAt(i) == '-')
                   nueva +=  Character.toString(frase.charAt(i));
               
               else
                   nueva += valor.get(frase.charAt(i));
           }
           System.out.println(nueva);
           
       }
        
    }
}