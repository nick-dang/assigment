import javafx.collections.FXCollections;
import javafx.scene.control.Label;
import javafx.scene.control.ListView;
import javafx.scene.layout.Pane;

public class DVDCollectionAppView1 extends Pane implements DVDView{
    private ListView<String>    tList;
    private ListView<Integer>   yList, lList;
    private DVDButtonPane       buttonPane;

    public ListView<String> getTitleList() { return tList; }
    public ListView<Integer> getYearList() { return yList; }
    public ListView<Integer> getLengthList() { return lList; }
    public DVDButtonPane getButtonPane() { return buttonPane; }

    public DVDCollectionAppView1() {
            // Create the labels
            Label label1 = new Label("Title");
            label1.relocate(10, 10);
            Label label2 = new Label("Year");
            label2.relocate(220, 10);
            Label label3 = new Label("Length");
            label3.relocate(290, 10);

            // Create the lists
            tList = new ListView<String>();
            tList.relocate(10, 40);
            tList.setPrefSize(200,150);

            yList = new ListView<Integer>();
            yList.relocate(220, 40);
            yList.setPrefSize(60,150);

            lList = new ListView<Integer>();
            lList.relocate(290, 40);
            lList.setPrefSize(60,150);

            // Create the button pane
            buttonPane = new DVDButtonPane();
            buttonPane.relocate(30, 200);
            buttonPane.setPrefSize(305,30);

            // Add all the components to the Pane
            getChildren().addAll(label1, label2, label3, tList, yList, lList, buttonPane);

            setPrefSize(360, 240);
        }


    public void update(DVDCollection model, int selectedDVD) {
        String[] titleArray = new String [model.getDvdCount()];
        Integer[] yearArray = new Integer [model.getDvdCount()];
        Integer[] lengthArray = new Integer [model.getDvdCount()];
        for (int i = 0; i < model.getDvdCount(); i++){
            titleArray[i] = model.getDVDList()[i].getTitle();
            yearArray[i] = model.getDVDList()[i].getYear();
            lengthArray[i] = model.getDVDList()[i].getDuration();
        }
        //put the arrays of titles, years and length onto the views of each and highlight the selected one
        tList.setItems(FXCollections.observableArrayList(titleArray));
        yList.setItems(FXCollections.observableArrayList(yearArray));
        lList.setItems(FXCollections.observableArrayList(lengthArray));
        tList.getSelectionModel().select(selectedDVD);
        yList.getSelectionModel().select(selectedDVD);
        lList.getSelectionModel().select(selectedDVD);


    }
}