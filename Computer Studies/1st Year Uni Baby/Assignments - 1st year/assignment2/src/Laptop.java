public class Laptop extends ComputerSpecs{
    private int screenSize;

    public Laptop(double price, int quantity, double cpuSpeed, int ram, boolean ssd, int storage, int screenSize){
        super(price, quantity, cpuSpeed, ram, ssd, storage);
        this.screenSize = screenSize;
    }

    public String toString(){
        if (ssd){
            return screenSize + "\" Laptop PC with " + cpuSpeed + "ghz CPU, " + ram + "GB RAM, " + storage + "GB SSD drive "+
                    "(" + price + " dollars each, " + stockQuantity + " in stock, " + soldQuantity + " sold)";
        }
        return screenSize + "\" Laptop PC with " + cpuSpeed + "ghz CPU, " + ram + "GB RAM, " + storage + "GB HDD drive "+
                "(" + price + " dollars each, " + stockQuantity + " in stock, " + soldQuantity + " sold)";
    }

}

