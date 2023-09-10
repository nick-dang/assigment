import javafx.scene.control.Button;
import javafx.scene.layout.Pane;

public class ElectronicStoreButtonPane extends Pane {
    private Button resetStore, add, remove, complete;
    public Button getResetStore(){return resetStore;}
    public Button getAdd(){return add;}
    public Button getRemove(){return remove;}
    public Button getComplete(){return complete;}

    public ElectronicStoreButtonPane(){
        Pane apane = new Pane();

        //create the buttons
        add = new Button("Add to Cart");
        add.relocate(240, 335);
        add.setPrefSize(120,40);
        add.setDisable(true);

        resetStore = new Button("Reset Store");
        resetStore.relocate(25, 335);
        resetStore.setPrefSize(120,40);

        remove = new Button("Remove from Cart");
        remove.relocate(475, 335);
        remove.setPrefSize(120,40);
        remove.setDisable(true);

        complete = new Button("Complete Sale");
        complete.relocate(595, 335);
        complete.setPrefSize(120,40);
        complete.setDisable(true);
        apane.getChildren().addAll(add,resetStore,remove,complete);
        getChildren().addAll(apane);
    }
}
