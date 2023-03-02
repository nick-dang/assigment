public class Fridge {
    double fridgeSize;
    boolean freezer; 
    String colour; 

    public Fridge (double fridgeSize, boolean freezer, String colour){
        this.fridgeSize = fridgeSize;
        this.freezer = freezer;
        this.colour = colour;
    }

    public String toString(){
        String name = this.fridgeSize + " cubic foot Fridge ";

        if (freezer){
            return name + "with Freezer (" + colour + ")";
        }
        return name + "(" + colour + ")";
    }
}
