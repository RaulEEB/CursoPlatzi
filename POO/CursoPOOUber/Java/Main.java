
class Main{
    public static void main(String[] args) {
        System.out.println("Hola mundo");
        Account account = new Account("Andrea Herrera","70585583");
        Car car = new Car("AMQ123",account);
        
        car.printDataCar();

        Account account2 = new Account("Andres Herrera","70585584");
        Car car2 = new Car("QWE567",account2);
        
        car2.printDataCar();
    }
}