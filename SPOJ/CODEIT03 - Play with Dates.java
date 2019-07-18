import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Calendar;
import java.util.GregorianCalendar;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st = new StringTokenizer("");
    static PrintWriter out = new PrintWriter(System.out);
    public static void main(String[] args)throws IOException{
        int casos = nextInt();
        while (casos-->0) {
            int dia = nextInt();
            int mes = nextInt();
            int año = nextInt();
            GregorianCalendar fecha = new GregorianCalendar(año,mes-1,dia);
            int diaSemana = fecha.get(Calendar.DAY_OF_WEEK);
            String[] dias = {
                    "Sunday",
                    "Monday",
                    "Tuesday",
                    "Wednesday",
                    "Thursday",
                    "Friday",
                    "Saturday"
            };

            out.println(dias[diaSemana-1]);



        }
        out.close();

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
