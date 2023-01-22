import java.util.Scanner;

public class Main1 {
    public static void main(String[] args) {
        int op=10;
        Scanner sc = new Scanner(System.in);
        while(op!=0){
            System.out.println("************************");
            System.out.println("Digite a opção desejada:");
            System.out.println("*1 para operador 'E'   *");
            System.out.println("*2 para operador 'OU'  *");
            System.out.println("*0 para sair           *");
            System.out.println("************************");
            op = sc.nextInt();
            switch (op){
                case 0:
                    break;
                case 1:
                    E1 e = new E1();
                    e.mostraTabela();
                    break;
                case 2:
                    OU1 ou = new OU1();
                    ou.mostraTabela();
                    break;
                default:
                    System.out.println("*    Opção inválida    *");
                    break;
            }
        }
        sc.close();
    }
}
