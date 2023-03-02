public class ElectronicStore {
    private String name;
    private double revenue;
    private Product[] products;
    final int MAX_PRODUCTS = 10;
    public ElectronicStore(String name) {
        this.name = name;
        revenue = 0;
        products = new Product[MAX_PRODUCTS];
    }
    public String getName(){return name;}

    public boolean addProduct(Product p){
        for (int i = 0; i < MAX_PRODUCTS; i++) {
            if (products[i] == null) {
                products[i] = p;
                return true;
            }
        }
        return false;
    }

    public boolean sellProducts(int proToSell, int numToSell){
        if (proToSell >= 0 && proToSell <= MAX_PRODUCTS &&products[proToSell] != null && numToSell > 0){
            revenue += products[proToSell].sellUnits(numToSell);
            return true;
        }
        return false;
    }

    public double getRevenue(){return revenue;}
    public void printStock() {
        System.out.println("The store has the following:");
        for (int i = 0; i < products.length; i++) {
            if (products[i] != null){
                System.out.println(i + ". " + products[i].toString());
            }

        }
    }


}