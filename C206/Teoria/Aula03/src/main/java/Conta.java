public class Conta {

    double saldo, limite;
    Cliente cliente;

    void sacar(double quantia){
        saldo -= quantia;
    }
    void deposito(double quantia){
        saldo += quantia;
    }
}
