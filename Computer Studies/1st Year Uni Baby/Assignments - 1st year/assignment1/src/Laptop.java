public class Laptop {
    double cpu;
    int ram;
    int storage;
    boolean ssd;
    int screenSize;

    public Laptop(double cpu, int ram, int storage, boolean ssd, int screenSize){
        this.cpu = cpu;
        this.ram = ram;
        this.storage = storage;
        this.ssd = ssd;
        this.screenSize = screenSize;
    }

    public String toString(){
        if (ssd){
            return screenSize + "\" Laptop PC with " + cpu + "ghz CPU, " + ram + "GB RAM, " + storage + "GB SSD drive";
        }
        return screenSize + "\" Laptop PC with " + cpu + "ghz CPU, " + ram + "GB RAM, " + storage + "GB HDD drive";
    }

}

