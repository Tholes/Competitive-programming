
import java.io.DataInputStream;
import java.io.DataOutputStream;

public class Main {

    public static void main(String[] args) throws Exception {
        DataInputStream in = new DataInputStream(System.in);
        DataOutputStream out = new DataOutputStream(System.out);
        
        int codigo;
        while ((codigo = in.read()) != -1) {
            if(codigo== 10)
                out.writeByte(10);               
            
            else
                out.writeByte(codigo - 7);                       
        }
        out.flush();       
    }
}