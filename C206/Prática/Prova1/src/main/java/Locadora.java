public class Locadora {
    String nome;
    String CNPJ;
    String endereco;
    int carrosParaAlugar;
    Carro carro[];

    public Locadora(){

        carro = new Carro[5];
    }

    boolean flagg = true;
    void adicionarCarro(Carro carro){

        for (int i = 0;i< this.carro.length+1;i++) {

            if(this.carro[i] == null && flagg == true){
                this.carro[i] = carro;
                System.out.println("Carro adicionado");
                flagg = true;
                return;
            }
        }
        flagg = false;
        for (int i = 0;i< this.carro.length;i++) {

            if(this.carro[i]!=null && flagg == false){
                System.out.println("Cheio");
                return;
            }
        }




    }
    public void mostraInfo() {
        System.out.println("Nome da plataforma: " + nome);
        System.out.println("CNPJ: " + CNPJ);
        System.out.println("Nome da plataforma: " + endereco);
        System.out.println("Carros para alugar: " + carrosParaAlugar);
        for (int i = 0; i < carro.length; i++) {
            if (carro[i] != null) {
                System.out.println("Posicao: " + i);
                System.out.println("Nome: " + carro[i].modelo);
                System.out.println("Preco: " + carro[i].cor);
                System.out.println("Está alugado ? " + carro[i].alugado);
            }

        }
    }
    float contarCarrosParaAlugar() {
        float resultado = 0;
        int truee = 0;
        int conta = 0;
        for (int i = 0; i < this.carro.length; i++) {

            if (this.carro[i] != null) {
                conta++;
                if (carro[i].alugado == true) {
                    truee++;
                }
            }
            System.out.println(truee);
            resultado = (truee * 100) / (conta);

        }
        return resultado;
    }
    void alugarCarro(int index){
        for (int i = 0; i < carro.length; i++) {
            if (index == i) {
                carro[i].alugado = false;
                System.out.println("Carro alugado com sucesso.");
            }

        }
    }

}
