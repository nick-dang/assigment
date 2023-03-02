public class Product {
    double price;
    int stockQuantity;
    int soldQuantity;
    public Product (double price, int stockQuantity){
        this.price = price;
        this.stockQuantity = stockQuantity;
        soldQuantity = 0;
    }
    public double sellUnits(int amount){
        double revenue = 0;
        if (amount <= stockQuantity){
            revenue = amount * price;
            stockQuantity -= amount;
            soldQuantity += amount;
        }
        return revenue;
    }
}
