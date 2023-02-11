public class ElectronicStore {
    String name;
    static int maxItem = 3;
    Desktop[] desktop = new Desktop[maxItem];

    Laptop[] laptop = new Laptop[maxItem];

    Fridge[] fridge = new Fridge[maxItem];

    public ElectronicStore(String name) {
        this.name = name;
        desktop[0] = new Desktop(3.2, 8, 500, true);
        desktop[1] = new Desktop(2.8, 16, 1000, false);
        desktop[2] = new Desktop(4.0, 32, 2000, true);
        laptop[0] = new Laptop(2.4, 4, 250, true, 15);
        laptop[1] = new Laptop(2.8, 8, 500, false, 17);
        laptop[2] = new Laptop(3.0, 12, 1000, true, 14);
        fridge[0] = new Fridge(15.6, true, "white");
        fridge[1] = new Fridge(10.5, false, "green");
        fridge[2] = new Fridge(20.0, true, "pink");
    }

    public void printStock() {
        System.out.println("The store has the following:");
        for (int i = 0; i < maxItem; i++) {
            System.out.print(desktop[i] + "\n" + laptop[i] + "\n" + fridge[i] + "\n");
        }
       
    }

    public boolean searchStock(String search) {
        search = search.toLowerCase();
        for (int i = 0; i < maxItem; i++) {
            if (desktop[i].toString().toLowerCase().contains(search)
                    || laptop[i].toString().toLowerCase().contains(search)
                    || fridge[i].toString().toLowerCase().contains(search)) {
                return true;
            }
        }
        return false;
    }

}