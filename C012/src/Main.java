import java.util.Random;
import java.util.Scanner;
public class Main {
    public static int aleatoriar(int minimo, int maximo) {
        Random random = new Random();
        return random.nextInt((maximo - minimo) + 1) + minimo;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int i;
        String nome;
        int midi;
            System.out.println("----------------------------------");
            System.out.println("Escolha uma opção:");
            System.out.println("1 - Do do programa");
            System.out.println("2 - Medição de Midi-Chlorians");
            System.out.println("0 - Sair");
            System.out.println("-----------------------------");
            i = sc.nextInt();
            switch (i) {
                case 0:
                    break;
                case 1:
                    System.out.println("O objetivo deste programa é simular sua pontuação em Midi-Chlorians com base em seu nome.");
                    System.out.println("Em Coruscant, Anakin estava intrigado sobre o que eram essas tais midi-chlorians que tanto falaram a respeito na reunião do Conselho Jedi. Então ele perguntou a Qui-Gon Jinn, que disse:\n" +
                            "\n" +
                            "São seres de vidas microscópicas inteligentes que vivem no interior de suas células. Sem as midi-chlorians, a vida não poderia existir, e nós não teríamos conhecimento da Força. Elas continuamente conversam conosco, nos dizendo a vontade da Força. Quando você aprender a acalmar sua mente, escutará elas conversando com você.\n" +
                            "\n" +
                            "Ou seja, as midi-chlorians são um fator essencial para a existência de vida na galáxia.");
                    break;
                case 2:
                    System.out.println("Digite seu nome:");
                    if (sc.hasNextLine()) {
                        sc.nextLine();
                    }
                    nome = sc.nextLine();
                    Thread T1 = new Thread(nome);
                    T1.start();
                    String Pega = String.valueOf(nome.charAt(0));
                    if (Pega.equals("A") || Pega.equals("F") || Pega.equals("K") || Pega.equals("P") || Pega.equals("U") || Pega.equals("Z")) {
                        midi = aleatoriar(0, 5950);
                        if (midi <= 3100) {
                            System.out.println("Sua contagem " + midi + " se aproxima mais de Han Solo (1500 Midi-Chlorians)! ");
                        } else if (midi > 3101 && midi <= 4700) {
                            System.out.println("Sua contagem " + midi + " se aproxima mais de Padmé Amidala (4700 Midi-Chlorians)! ");
                        } else if (midi > 4701 && midi <= 5950) {
                            System.out.println("Sua contagem " + midi + " se aproxima mais de Padmé Amidala (4700 Midi-Chlorians)! ");
                        }
                    } else if (Pega.equals("B") || Pega.equals("G") || Pega.equals("L") || Pega.equals("Q") || Pega.equals("V")) {
                        midi = aleatoriar(5951, 12000);
                        if (midi >= 5951 && midi < 7200) {
                            System.out.println("Sua contagem " + midi + " se aproxima mais de Chewbacca (7200 Midi-Chlorians)! ");
                        } else if (midi > 7201 && midi <= 8600) {
                            System.out.println("Sua contagem " + midi + " se aproxima mais de Chewbacca (7200 Midi-Chlorians)! ");
                        } else if (midi > 8601 && midi <= 10000) {
                            System.out.println("Sua contagem " + midi + " se aproxima mais de Qui-Gon Jinn (10000 Midi-Chlorians)! ");
                        } else if (midi > 10001 && midi <= 11000) {
                            System.out.println("Sua contagem " + midi + " se aproxima mais de Qui-Gon Jinn (10000 Midi-Chlorians)! ");
                        } else if (midi > 11001 && midi <= 12000) {
                            System.out.println("Sua contagem " + midi + " se aproxima mais de Darth Maul (12000 Midi-Chlorians)! ");
                        }
                    } else if (Pega.equals("C") || Pega.equals("H") || Pega.equals("M") || Pega.equals("R") || Pega.equals("W")) {
                        midi = aleatoriar(12001, 17700);
                        if (midi >= 12001 && midi < 12700) {
                            System.out.println("Sua contagem " + midi + " se aproxima mais de Darth Maul (12000 Midi-Chlorians)! ");
                        }
                        else if (midi > 12701 && midi <= 13400) {
                            System.out.println("Sua contagem " + midi + " se aproxima mais de Obi-Wan Kenobi (13400 Midi-Chlorians)! ");
                        }
                        else if (midi > 13401 && midi <= 13950) {
                            System.out.println("Sua contagem " + midi + " se aproxima mais de Obi-Wan Kenobi (13400 Midi-Chlorians)! ");
                        }
                        else if (midi > 13951 && midi <= 14500) {
                            System.out.println("Sua contagem " + midi + " se aproxima mais de Luke Skywalker (14500 Midi-Chlorians)! [Aquele que anda no céu]");
                        }
                        else if (midi > 14501 && midi <= 16100) {
                            System.out.println("Sua contagem " + midi + " se aproxima mais de Luke Skywalker (14500 Midi-Chlorians)! [Aquele que anda no céu]");
                        }
                        else if (midi > 16101&& midi <= 17700) {
                            System.out.println("Sua contagem " + midi + " se aproxima mais de Mestre Yoda (17700 Midi-Chlorians)!");
                        }
                    } else if (Pega.equals("D") || Pega.equals("I") || Pega.equals("N") || Pega.equals("S") || Pega.equals("X")) {
                        midi = aleatoriar(17701, 24000);
                        if (midi > 17701&& midi <= 19100) {
                            System.out.println("Sua contagem " + midi + " se aproxima mais de Mestre Yoda (17700 Midi-Chlorians)!");
                        }
                        else if (midi > 19101&& midi <= 20500) {
                            System.out.println("Sua contagem " + midi + " se aproxima mais de Palpatine/Darth Sidious (20500 Midi-Chlorians)!");
                        }
                    } else if (Pega.equals("E") || Pega.equals("J") || Pega.equals("O") || Pega.equals("T") || Pega.equals("Y")) {
                        midi = aleatoriar(20501, 30000);
                        if (midi > 20501 && midi <= 24100) {
                            System.out.println("Sua contagem " + midi + " se aproxima mais de Palpatine/Darth Sidious (20500 Midi-Chlorians)!");
                        }else if (midi > 24101) {
                            System.out.println("Sua contagem " + midi + " se aproxima mais de Anakin Skywalker/Darth Vader (27700 Midi-Chlorians)!");
                        }
                    }
                    break;
                default:
                    System.out.println("Opção inválida");

            }



    }
}
/* A contagem não é oficial e foi estimada pelo site https://sociedadejedi.com.br/2017/04/04/anakin-lidera-o-ranking-de-contagem-midi-chlorian-veja-a-lista/

 */