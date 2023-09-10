import javafx.application.Application;
import javafx.collections.FXCollections;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.Scene;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.Pane;
import javafx.stage.Stage;

import java.util.ArrayList;
import java.util.List;

public class ElectronicStoreApp extends Application {
    private ElectronicStore model;

    public ElectronicStoreApp(){
        model = ElectronicStore.createStore();
    }
    public void start(Stage primaryStage){
        Pane aPane = new Pane();

        ElectronicStoreView view = new ElectronicStoreView();

        view.getStoreList().setOnMousePressed(new EventHandler<MouseEvent>() {
            public void handle(MouseEvent mouseEvent) {
                view.getButton().getAdd().setDisable(false);
            }
        });

        view.getButton().getAdd().setOnAction(new EventHandler<ActionEvent>() {
            public void handle(ActionEvent actionEvent) {
                int select = view.getStoreList().getSelectionModel().getSelectedIndex();

                model.getStock()[select].sellUnits(1);
                view.update(model, select);
            }
        });




        aPane.getChildren().add(view);
        view.update(model,-1); //put it negative so that it doesn't add anything into the cart list
        primaryStage.setTitle(model.getName());
        primaryStage.setResizable(false);
        primaryStage.setScene(new Scene(aPane));
        primaryStage.show();
    }

    public static void main(String [] args) {launch (args);}
}
