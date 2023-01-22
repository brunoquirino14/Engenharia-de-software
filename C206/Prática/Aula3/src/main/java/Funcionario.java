public class Funcionario {
    int idade;
    String cpf;
    String nome;
    double salario;

    public Funcionario(String nome, int idade, String cpf){
        this.nome = nome;
        this.cpf = cpf;
        this.idade = idade;
    }

    void tirarFerias(String mes){
        System.out.println("Funcionario" + nome + " vai tirar férias em " + mes);
    }

    double calculaSalarioAnual(){
        return 12*salario;
    }
}
