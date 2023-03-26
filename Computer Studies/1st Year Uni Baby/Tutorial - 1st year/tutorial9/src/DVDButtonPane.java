import javafx.scene.control.Button;

import javafx.scene.layout.Pane;


public class DVDButtonPane extends Pane {
    private Button addButton;
    private Button deleteButton;
    private Button statButton;
    public DVDButtonPane(){
        Pane innerPane = new Pane();


        addButton = new Button("Add");
        addButton.relocate(10,200);
        addButton.setPrefSize(90,30);
        addButton.setStyle("-fx-font: 12 arial; -fx-base: rgb(3,102,3); " +"-fx-text-fill: rgb(255,255,255);");

        deleteButton = new Button("Delete");
        deleteButton.relocate(110,200);
        deleteButton.setPrefSize(90,30);
        deleteButton.setStyle("-fx-font: 12 arial; -fx-base: rgb(195,5,5); " +"-fx-text-fill: rgb(255,255,255);");

        statButton = new Button("Stats");
        statButton.relocate(220,200);
        statButton.setPrefSize(90,30);
        statButton.setStyle("-fx-font: 12 arial; -fx-base: rgb(234,234,234); " +"-fx-text-fill: rgb(0,0,0);");
        innerPane.getChildren().addAll(addButton,deleteButton,statButton);
        getChildren().addAll(innerPane);
    }
    public Button getAddButton(){return addButton;}
    public Button getDeleteButton(){return deleteButton;}
    public Button getStatButton(){return statButton;}
}
