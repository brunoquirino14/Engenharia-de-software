package br.inatel.cdg.Calculadora;

public class Calculadora {
    public static double PI = 3.14;
    private static int qtdVezUsada = 0;

    public static double circunferencia(double raio){
        qtdVezUsada++;
        return PI*(raio*raio);
    }

    public static double volume(double raio){
        qtdVezUsada++;
        return (4.0/3.0)*PI*(raio*raio*raio);
    }

    public static int getQtdVezUsada() {
        return qtdVezUsada;
    }

    public static void setPI(double PI) {
        Calculadora.PI = PI;
    }
}
