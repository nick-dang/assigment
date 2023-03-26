import javafx.application.Application;
import javafx.collections.FXCollections;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.ListView;
import javafx.scene.layout.Pane;
import javafx.stage.Stage;



public class DVDCollectionApp1 extends Application {
    public void start(Stage primaryStage) {
        Pane aPane = new Pane();

        Label label1 = new Label("Title");
        label1.relocate(10,10);
        Label label2 = new Label("Year");
        label2.relocate(220,10);
        Label label3 = new Label("Length");
        label3.relocate(290,10);
        // Create the lists
        String[]    titles = {"Star Wars", "Java is cool", "Mary Poppins", "The Green Mile"};
        String[]    years = {"1978", "2002", "1968", "1999"};
        String[]    lengths = {"124", "93", "126", "148"};
        // ... ADD CODE HERE ... //
        ListView<String> titleView = new ListView<>();
        titleView.setItems(FXCollections.observableArrayList(titles));
        titleView.relocate(10,40);
        titleView.setPrefSize(200,150);

        ListView<String> yearView = new ListView<>();
        yearView.setItems(FXCollections.observableArrayList(years));
        yearView.relocate(220,40);
        yearView.setPrefSize(60,150);

        ListView<String> lengthView = new ListView<>();
        lengthView.setItems(FXCollections.observableArrayList(lengths));
        lengthView.relocate(290,40);
        lengthView.setPrefSize(60,150);

        DVDButtonPane myButton = new DVDButtonPane();
        myButton.relocate(20,0);
        // Don't forget to add the components to the window, set the title,
        // make it non-resizable, set Scene dimensions and then show the stage
        // ... ADD CODE HERE ... //

        aPane.getChildren().addAll(label1,label2,label3,titleView,yearView,lengthView,myButton);
        primaryStage.setTitle("My DVD Collection");
        primaryStage.setScene(new Scene(aPane, 360, 240));
        primaryStage.setResizable(false);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }

}
