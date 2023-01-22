
import java.util.Scanner;
public class Main {
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        int escolha=0;
        int certo;
        Plataforma pla = new Plataforma();
        System.out.println("Digite o nome da plataforma: ");
        pla.nome = sc.nextLine();
        System.out.println("O nome está correto ? Digite 0 para sim e 1 para nao");
        certo = sc.nextInt();
        while (certo == 1){
            System.out.println("Digite o nome da plataforma: ");
            sc.nextLine();
            pla.nome = sc.nextLine();
            System.out.println("O nome está correto ? Digite 0 para sim e 1 para nao");
            certo = sc.nextInt();
        }
        certo = 0;
        System.out.println("Digite o nome do criador da plataforma: ");
        sc.nextLine();
        pla.criador = sc.nextLine();
        System.out.println("O nome está correto ? Digite 0 para sim e 1 para nao");
        certo = sc.nextInt();
        while (certo == 1){
            System.out.println("Digite o nome do criador: ");
            sc.nextLine();
            pla.criador = sc.nextLine();
            System.out.println("O nome está correto ? Digite 0 para sim e 1 para nao");
            certo = sc.nextInt();
        }
        while(escolha!=10){
            System.out.println("Menu:");
            System.out.println("1 - Adicionar jogo");
            System.out.println("2 - Mostra informacao");
            System.out.println("3 - Consultar jogos mais barato e mais caro");
            System.out.println("4 - Mostrar quantidade de jogos com dlc");
            System.out.println("-----------------------------------");
            escolha = sc.nextInt();

            switch (escolha){

                case 1:

                    Jogo I1 = new Jogo();
                    System.out.print("Escreva o nome: ");
                    sc.nextLine();
                    I1.nome = sc.nextLine();



                    System.out.print("Escreva o preco: ");
                    I1.preco = sc.nextDouble();

                    System.out.print("Escreva o genero : ");
                    sc.nextLine();
                    I1.genero = sc.nextLine();



                    System.out.print("Tem dlc ? - true para sim ou false para nao: ");
                    I1.dlc= sc.nextBoolean();



                    pla.adicionarJogo(I1);

                    break;

                case 2:
                    pla.mostraInfo();
                    break;

                case 3:
                    pla.mostraMaisBaratoMaisCaro();
                    break;
                case 4:
                    pla.calculaDlc();
                    break;
                case 10:
                    break;

            }

        }

    }
}
