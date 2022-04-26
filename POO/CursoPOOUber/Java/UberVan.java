import java.util.ArrayList;
import java.util.Map;

public class UberVan extends Car{
    Map<String, Map<String, Integer>> typeCarAccepted;
    ArrayList<String> seatsMaterial;
    private Integer passenger;


    public UberVan(String license, Account driver, Map<String, 
    Map<String, Integer>> typeCarAccepted, 
    ArrayList<String> seatsMaterial ){
        super(license, driver);
        this.typeCarAccepted = typeCarAccepted;
        this.seatsMaterial = seatsMaterial;
    }

    @Override
    public void setPassegenger(Integer passegenger) {
        if(passegenger == 6){
            this.passenger = passegenger;
        }else{
            System.out.println("Neceistas 6 asientos");
        }


    }
}
