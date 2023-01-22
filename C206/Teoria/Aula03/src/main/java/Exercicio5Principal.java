import java.util.Scanner;
public class Exercicio5Principal {

    public static void main(String[] args){
        Scanner ler = new Scanner(System.in);
        System.out.println("Escreva o nome do Ashen: ");
        String n = ler.nextLine();
        Ashen a = new Ashen();
        a.nome = n;

        a.vida = 100;
        //System.out.println(a.nome);
        Arma b = new Arma();

        void usarArma(double res){
            b.resistencia = b.resistencia-2
        }

    }
}
