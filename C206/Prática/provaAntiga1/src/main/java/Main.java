public class Main {
    public static void main(String[] args) {
        Deck d1 = new Deck();
        d1.dono = "Sheldon";

        Carta c1 = new Carta();
        c1.nome = "Leinden";
        c1.poder = 25;
        c1.clssificacao = "Soldado";

        Carta c2 = new Carta();
        c2.nome = "Frost";
        c2.poder = 21;
        c2.clssificacao = "Arqueiro";

        Carta c3 = new Carta();
        c3.nome = "Guild";
        c3.poder = 7;
        c3.clssificacao = "Arqueiro";

        Carta c4 = new Carta();
        c4.nome = "Gulover";
        c4.poder = 16;
        c4.clssificacao = "Pesado";

        d1.adicionarCarta(c1);
        d1.adicionarCarta(c2);
        d1.adicionarCarta(c3);
        d1.adicionarCarta(c4);

        d1.mostrarInfo();

        d1.calcularPderMedio();

        d1.calculaClassificacao();

    }
}