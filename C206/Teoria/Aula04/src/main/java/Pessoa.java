import lombok.Data;

@Data
public class Pessoa {

    private double peso, imc, temp;
    private int idade, cpf;
    private String nome, descricao;
}
