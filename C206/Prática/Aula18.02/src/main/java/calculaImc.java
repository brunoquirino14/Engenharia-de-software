public class calculaImc {
    double calcula(double peso, double altura){
        double res=0;
        res = peso/(altura*altura);
        return res;
    }
}
