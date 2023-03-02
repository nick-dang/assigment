public class Oven extends KitchenSpecs{
    private boolean convection;

    public Oven (double price, int quantity, int wattage, String color, String brand, boolean convection){
        super(price, quantity, wattage, color, brand);
        this.convection = convection;
    }

    public String toString(){
        String name = brand + " Oven ";
        if (convection){
            return name + (" with convection " + "(" + color + ", " + wattage + " watts) (" + price + " dollars each, " +
                    stockQuantity + " in stock, " + soldQuantity + " sold)");
        }
        return name + ("(" + color + ", " + wattage + " watts) (" + price + " dollars each," +
                stockQuantity + " in stock, " + soldQuantity + " sold)");
    }
}