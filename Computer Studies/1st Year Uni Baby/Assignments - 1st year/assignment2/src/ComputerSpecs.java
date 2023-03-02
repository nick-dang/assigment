public class ComputerSpecs extends  Product{
    double cpuSpeed;
    int ram;
    boolean ssd;
    int storage;
    public ComputerSpecs(double price, int quantity, double cpuSpeed, int ram, boolean ssd, int storage){
        super(price, quantity);
        this.ram = ram;
        this.cpuSpeed = cpuSpeed;
        this.ssd = ssd;
        this.storage = storage;
    }
}
