public class Principal {
    public static void main(String[] args) {

        Conta[] contas = new Conta[3];

        Conta c1 = new Conta();
        c1.saldo = 200;
        c1.nome = "Matheus";
        c1.mostraInfo();
        contas[0] = c1;


        Conta c2 = new Conta();
        c2.saldo = 100;
        c2.nome = "Bruno";
        c2.mostraInfo();

        for (int i=0; i< contas.length;i++){// for para acessar posição de vetores
            if (contas[i]!=null)
            contas[i].mostraInfo();
        }
        for (Conta item : contas){//for para varrer valores
            if (item !=null)
                item.mostraInfo();
        }
    }
}
