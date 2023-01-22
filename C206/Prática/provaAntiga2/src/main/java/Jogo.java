
public class Jogo {
    String nome;
    String genero;
    Double preco;
    boolean dlc;
    Jogo jogos[];

    void mostraInf(){
        for (int i = 0; i < jogos.length; i++) {
            if (jogos[i] != null) {
                System.out.println("Posicao: " + i);
                System.out.println("Nome: " + jogos[i].nome);
                System.out.println("Preco: " + jogos[i].preco);
                System.out.println("Genero: " + jogos[i].genero);
                System.out.println("Possui DLC?: " + jogos[i].dlc);
            }

        }
    }

}
