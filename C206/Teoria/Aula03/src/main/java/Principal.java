public class Principal {
    public static void main(String[] args){
        Conta c = new Conta();
        c.saldo = 250;
        c.limite = 10;
        Cliente cliente = new Cliente();

        c.cliente.nome = "Caroline";
        c.cliente.cpf = "123";
        c.cliente.idade = 15;

        System.out.println(c.cliente.nome);



    }
}
