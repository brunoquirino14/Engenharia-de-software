public class Kart {
    String nome;
    Piloto p;
    Motor m;

    public Kart(){
        m = new Motor();
    }

    public void pular(){
        System.out.println("Pulei");
    }
    public void soltarTurbo(){
        System.out.println("MODO TURBOOOOOOOOOOOOOOOOOO");
    }
    public void fazerDrift(){
        System.out.println("Drift no grauuuuuuuuuuu");
    }

}
