public class Main {

    public static void main(String[] args){
        Funcionario f1 = new Funcionario("Bruni", 23, "1233");

        //f1.nome = "Bruno";
        //f1.cpf = "123";
        f1.salario = 2000;
        //f1.idade = 22;


        f1.tirarFerias("Janeiro");
        System.out.println(f1.calculaSalarioAnual());
    }
}
