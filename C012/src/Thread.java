public class Thread extends java.lang.Thread {
    String name;
    public Thread(String Nome){
        name = Nome;
    }
    public void run(){
        for (int i = 0; i<5;i++){
            System.out.println(name + " - "+i);

            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }

        }

    }
}
