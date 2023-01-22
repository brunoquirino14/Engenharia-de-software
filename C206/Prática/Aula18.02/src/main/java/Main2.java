import java.awt.desktop.AboutEvent;
import java.util.Scanner;

public class Main2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int op = 10;
        do{
            System.out.println("************************");
            System.out.println("Digite seu peso:");
            double peso = sc.nextDouble();
            System.out.println("Digite sua altura:");
            double altura = sc.nextDouble();
            System.out.println("*************************");
            System.out.println("Digite a opção desejada: ");
            System.out.println("*1 para calcular seu IMC*");
            System.out.println("*0 para sair            *");
            System.out.println("*************************");
            op = sc.nextInt();
            switch (op){
                case 0:
                    break;
                case 1:
                    System.out.println("*************************");
                    calculaImc imc = new calculaImc();
                    double armazena = imc.calcula(peso,altura);
                    if(armazena <= 18.5){
                    System.out.println("*    Abaixo do peso     *");
                    }
                    if(armazena >= 18.6 && armazena <= 24.9){
                        System.out.println("*      Peso ideal       *");
                    }
                    if(armazena >= 25 && armazena <= 29.9){
                        System.out.println("*Levemente acima do peso*");
                    }
                    if(armazena >= 30 && armazena <= 34.9){
                        System.out.println("*Obesidade grau I       *");
                    }
                    if(armazena >= 35 && armazena <= 39.9){
                        System.out.println("*Obesidade grau II (severa)*");
                    }
                    if(armazena > 40){
                        System.out.println("*Obesidade grau III (mórbida)*");
                    }
                    break;
                default:
                    System.out.println("*    Opção inválida    *");
                    break;
            }
            System.out.println("*************************");
            System.out.println("Digite a opção desejada: ");
            System.out.println("*1 para calcular seu IMC*");
            System.out.println("*0 para sair            *");
            System.out.println("*************************");
            op = sc.nextInt();
        }while(op!=0);
        sc.close();
    }
}
