public class Fridge extends KitchenSpecs{
    private boolean hasFreezer;

    public Fridge (double price, int quantity, int wattage, String color, String brand, boolean hasFreezer){
        super(price,quantity, wattage, color, brand);
        this.hasFreezer = hasFreezer;
    }


    public String toString(){

        if (hasFreezer){
            return brand + " Fridge with Freezer (" + color + ", " + wattage + " watts) " +
                    "(" + price + " dollars each, " + stockQuantity + " in stock, " + soldQuantity + " sold)";
        }
        return brand + " Fridge (" + color + ", " + wattage + " watts) " +
                "(" + price + " dollars each, " + stockQuantity + " in stock, " + soldQuantity + " sold)";
    }
}
