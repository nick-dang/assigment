public class Desktop {
    double cpu;
    int ram;
    int storage;
    boolean ssd;

    public Desktop (double cpu, int ram, int storage, boolean ssd){
        this.cpu = cpu;
        this.ram = ram;
        this.storage = storage;
        this.ssd = ssd;
    }



    public String toString(){
        if (ssd){
            return "Desktop PC with " + cpu + "ghz CPU, " + ram + "GB RAM, " + storage + "GB SSD drive";
        }
        return "Desktop PC with " + cpu + "ghz CPU, " + ram + "GB RAM, " + storage + "GB HDD drive";
    }
}
