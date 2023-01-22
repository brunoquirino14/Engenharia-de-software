import java.sql.SQLOutput;

public class Deck {
    String dono;
    Carta cartas[];

    public Deck(){

        cartas = new Carta[15];
    }

    void adicionarCarta(Carta carta){
        boolean  flag = true;
        for (int i = 0;i< cartas.length;i++){
            if(cartas[i] == null && flag){
                cartas[i] = carta;
                flag = false;
                System.out.println("Carta adicionada");
            }
            if (flag)
                System.out.println("Sem espaco no deck");
        }

    }

    void mostrarInfo(){
        System.out.println("Dono do deck: " + dono);
        for (Carta carta:cartas){
            if (carta != null)
                carta.mostraInfo();
        }
    }

    void calcularPderMedio(){
        int poder = 0;
        int totalCartas = 0;
        float medio = 0;
        for (Carta carta:cartas){
            if (carta != null){
                poder += carta.poder;
                totalCartas ++;
            }
        }
        System.out.println("Poder total: " + poder);
        medio = (float)poder/totalCartas;
        System.out.println("Poder medio: " + medio);
    }

    void calculaClassificacao() {
        int arqueiros = 0;
        int soldados = 0;
        int pesados = 0;
        for (Carta carta : cartas) {
            if (carta != null) {
                if (carta.clssificacao.equals("soldado"))
                    soldados++;
                else if (carta.clssificacao.equals("Arqueiros"))
                    arqueiros++;
                else
                    pesados++;
            }
        }
    }}
