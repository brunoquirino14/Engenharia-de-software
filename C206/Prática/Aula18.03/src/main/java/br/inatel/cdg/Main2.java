package br.inatel.cdg;

import br.inatel.cdg.Calculadora.Calculadora;

public class Main2 {
    public static void main(String[] args){
        System.out.println("Calculadora usada " + Calculadora.getQtdVezUsada()+" vezes");
        double raio = 6.0;
        System.out.println("Valor da circunferencia do raio " + raio+ ":"+Calculadora.circunferencia(raio));
        System.out.println("Valor da volume do raio " + raio+ ":"+Calculadora.volume(raio));
        System.out.println("Calculadora usada " + Calculadora.getQtdVezUsada()+" vezes");
        Calculadora.setPI(3.1415);
        System.out.println("Valor da circunferencia do raio " + raio+ ":"+Calculadora.circunferencia(raio));
        System.out.println("Valor da volume do raio " + raio+ ":"+Calculadora.volume(raio));
        System.out.println("Calculadora usada " + Calculadora.getQtdVezUsada()+" vezes");
    }
}
