
public class Plataforma {
    String nome;
    String criador;
    Jogo jogos[];
    int dlcss=0;


    public Plataforma(){

        jogos = new Jogo[10];
    }

    public void calculaDlc(){

        for (int i = 0; i < jogos.length; i++) {
            if (jogos[i] != null) {
                if(jogos[i].dlc == true){
                    dlcss++;



                }
            }

        }
        System.out.println("Quantidade de jogos com dlcs: " + dlcss);
        dlcss=0;

    }
    public void mostraInfo() {
        System.out.println("Nome da plataforma: " + nome);
        System.out.println("Criador: " + criador);
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

    void adicionarJogo(Jogo jogo){
        for (int i = 0;i< jogos.length;i++) {
            boolean flagg = true;
            if(jogos[i] == null && flagg == true){
                jogos[i] = jogo;
                System.out.println("Jogo adicionado");
                flagg=false;
                return;
            }
            if(jogos[i]!=null && flagg == false){
                System.out.println("Cheio");
            }
        }


    }
    //    void adicionarCarta(Carta carta){
    //        boolean  flag = true;
    //        for (int i = 0;i< cartas.length;i++){
    //            if(cartas[i] == null && flag){
    //                cartas[i] = carta;
    //                flag = false;
    //                System.out.println("Carta adicionada");
    //            }
    //            if (flag)
    //                System.out.println("Sem espaco no deck");
    //        }
    //
    //    }
    public void mostraMaisBaratoMaisCaro() {
        boolean  flag = true;
        double maiorValor=0;
        String armazenaNome1 = null;
        String armazenaNome2 = null;
        double menorValor=10000;
        for (int i = 0;i< jogos.length;i++){
            if(jogos[i] != null && flag == true){
                if(jogos[i].preco >= maiorValor) {
                    maiorValor = jogos[i].preco;
                    armazenaNome1 = jogos[i].nome;
                }
                if(jogos[i].preco <= menorValor) {
                    menorValor = jogos[i].preco;
                    armazenaNome2 = jogos[i].nome;
                }

            }
        }
        System.out.println("Jogo mais caro: "+ armazenaNome1);
        System.out.println("Jogo mais barato: "+armazenaNome2);
    }
    //boolean  flag = true;
    //        for (int i = 0;i< jogos.length;i++){
    //            if(jogos[i] == null && flag){
    //                jogos[i] = jogo;
    //                flag = false;
    //                System.out.println("Jogo adicionado");
    //            }
    //            if (flag)
    //                System.out.println("Plataforma cheia");
    //        }

}
