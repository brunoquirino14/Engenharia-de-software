import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

                Scanner sc = new Scanner(System.in);
                int escolha=0;
                int escolheCarro;
                Locadora loca = new Locadora();
                System.out.println("Digite o nome da locadora: ");
                loca.nome = sc.nextLine();
                System.out.println("Digite o CNPJ: ");
                loca.CNPJ = sc.nextLine();
                System.out.println("Digite o endereco: ");
                loca.endereco = sc.nextLine();
                System.out.println("Digite a quantidade de carros para aluguel: ");
                loca.carrosParaAlugar = sc.nextInt();

                while(escolha!=10){
                    System.out.println("Menu:");
                    System.out.println("1 - Adicionar carro");
                    System.out.println("2 - Mostra informacao");
                    System.out.println("3 - Consulta porcentagem de carros disponiveis");
                    System.out.println("4 - Alugar um carro");
                    System.out.println("10 - Sair");
                    System.out.println("-----------------------------------");
                    escolha = sc.nextInt();

                    switch (escolha){

                        case 1:

                            Carro I1 = new Carro();
                            System.out.print("Escreva a cor: ");
                            sc.nextLine();
                            I1.cor = sc.nextLine();

                            System.out.print("Escreva o modelo: ");
                            I1.modelo = sc.nextLine();

                            System.out.print("Esta alugado ? - true para sim ou false para nao: ");
                            I1.alugado= sc.nextBoolean();

                            loca.adicionarCarro(I1);

                            break;

                        case 2:
                            loca.mostraInfo();
                            break;

                          case 3:
                              System.out.println("Carros disponíveis para alugar: " + loca.contarCarrosParaAlugar() + "%");;
                          break;
                          case 4:
                              sc.nextLine();
                              System.out.print("Escolha a posicao do carro para alugar: ");
                              escolheCarro = sc.nextInt();
                            loca.alugarCarro(escolheCarro);
                              break;
                          case 10:
                             break;

                    }

                }

            }

}
