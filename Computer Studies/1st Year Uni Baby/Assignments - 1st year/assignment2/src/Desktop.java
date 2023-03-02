public class Desktop extends ComputerSpecs{
    private String profile;
    public Desktop (double price, int quantity, double cpuSpeed, int ram, boolean ssd, int
            storage, String profile){
        super(price,quantity,cpuSpeed,ram,ssd,storage);
        this.profile = profile;

    }



    public String toString(){
        if (ssd){
            return profile + " Desktop PC with " + cpuSpeed + "ghz CPU, " + ram + "GB RAM, " + storage + "GB SSD drive " +
                   "(" + price + " dollars each, " + stockQuantity + " in stock, " + soldQuantity + " sold)";
        }
        return "Desktop PC with " + cpuSpeed + "ghz CPU, " + ram + "GB RAM, " + storage + "GB HDD drive " +
                "(" + price + " dollars each, " + stockQuantity + " in stock, " + soldQuantity + " sold)";
    }
}
