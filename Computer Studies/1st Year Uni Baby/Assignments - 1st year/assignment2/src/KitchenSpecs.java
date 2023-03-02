public abstract class KitchenSpecs extends Product{
    int wattage;
    String color;
    String brand;

    public KitchenSpecs(double price, int quantity, int wattage, String color, String brand){
        super(price, quantity);
        this.wattage = wattage;
        this.color = color;
        this.brand = brand;
    }
}
