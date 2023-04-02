import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.Pane;
import javafx.stage.Stage;
import javafx.event.*;

import javax.swing.*;

public class DVDCollectionApp1  extends Application {
    private DVDCollection model;
    public DVDCollectionApp1() {
      model = DVDCollection.example1();
    }

    public void start(Stage primaryStage) {
        Pane  aPane = new Pane();

        // Create the view
        DVDCollectionAppView1  view = new DVDCollectionAppView1();
        aPane.getChildren().add(view);
        view.getButtonPane().getAddButton().setOnAction(new EventHandler<ActionEvent>() {
            public void handle(ActionEvent actionEvent) {
                String t = JOptionPane.showInputDialog("Enter song title");
                int y = Integer.parseInt(JOptionPane.showInputDialog("Enter the song's year"));
                int l = Integer.parseInt(JOptionPane.showInputDialog("Enter the song's duration"));
                model.add(new DVD(t,y,l));
                view.update(model,0);
            }
        });

        view.getButtonPane().getDeleteButton().setOnAction(new EventHandler<ActionEvent>() {
            public void handle(ActionEvent actionEvent) {
                String select = view.getTitleList().getSelectionModel().getSelectedItem();
                model.remove(select);
                view.update(model,0);

            }
        });

        view.getTitleList().setOnMousePressed(new EventHandler<MouseEvent>() {
            public void handle(MouseEvent mouseEvent) {
                int selectedIndex = view.getTitleList().getSelectionModel().getSelectedIndex();
                view.update(model,selectedIndex);
            }
        });


        view.update(model,0);
        primaryStage.setTitle("My DVD Collection");
        primaryStage.setResizable(false);
        primaryStage.setScene(new Scene(aPane));
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}