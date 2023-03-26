import javafx.application.Application;
import javafx.collections.FXCollections;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.ListView;
import javafx.scene.layout.Pane;
import javafx.stage.Stage;

public class DVDCollectionApp  extends Application {
    public void start(Stage primaryStage) {
        Pane  aPane = new Pane();

        // Create the labels
        // ... ADD CODE HERE ... //
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

        // Create the buttons
        // The following code shows how to set the font,
        // background color and text color of a button:
        // b.setStyle("-fx-font: 12 arial; -fx-base: rgb(0,100,0); " +
        //     "-fx-text-fill: rgb(255,255,255);");
        //the 3 rgb values represent the red/green/blue values for the color your want
        // ... ADD CODE HERE ... //
        Button addButton = new Button("Add");
        addButton.relocate(10,200);
        addButton.setPrefSize(95,30);
        addButton.setStyle("-fx-font: 12 arial; -fx-base: rgb(3,102,3); " +"-fx-text-fill: rgb(255,255,255);");

        Button deleteButton = new Button("Delete");
        deleteButton.relocate(115,200);
        deleteButton.setPrefSize(95,30);
        deleteButton.setStyle("-fx-font: 12 arial; -fx-base: rgb(195,5,5); " +"-fx-text-fill: rgb(255,255,255);");

        Button statButton = new Button("Stats");
        statButton.relocate(290,200);
        statButton.setPrefSize(60,30);
        statButton.setStyle("-fx-font: 12 arial; -fx-base: rgb(234,234,234); " +"-fx-text-fill: rgb(0,0,0);");
        // Don't forget to add the components to the window, set the title,
        // make it non-resizable, set Scene dimensions and then show the stage
        // ... ADD CODE HERE ... //

        aPane.getChildren().addAll(label1,label2,label3,titleView,yearView,lengthView,addButton,deleteButton,statButton);
        primaryStage.setTitle("My DVD Collection");
        primaryStage.setScene(new Scene(aPane, 360, 240));
        primaryStage.setResizable(false);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
