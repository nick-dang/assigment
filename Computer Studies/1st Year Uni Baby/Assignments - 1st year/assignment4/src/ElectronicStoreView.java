import javafx.collections.FXCollections;
import javafx.scene.control.Label;
import javafx.scene.control.ListView;
import javafx.scene.control.TextField;
import javafx.scene.layout.Pane;

import java.util.ArrayList;
import java.util.List;


public class ElectronicStoreView extends Pane {
    private ListView<String> storeList,cartList,popularList;
    private ElectronicStoreButtonPane button;
    private List<String> cartStock; //a local list to keep track the added product
    public ElectronicStoreView(){
        cartStock = new ArrayList<>();
        //create the labels
        Label label1 = new Label("Store Summary:");
        label1.relocate(40,10);

        Label label2 = new Label("# Sales:");
        label2.relocate(25,40);

        Label label3 = new Label("Revenue:");
        label3.relocate(25,70);

        Label label4 = new Label("$ / Sale:");
        label4.relocate(25,100);

        Label label5 = new Label("Most Popular Items:");
        label5.relocate(25,145);

        Label label6 = new Label("Store Stock:");
        label6.relocate(300,10);

        Label label7 = new Label("Current Cart:");
        label7.relocate(600,10);

        TextField numOfSale = new TextField();
        numOfSale.relocate(75,40);
        numOfSale.setPrefSize(100, 15);
        numOfSale.setText("0");
        TextField revenue = new TextField();
        revenue.relocate(75,70);
        revenue.setPrefSize(100, 15);
        revenue.setText("0.00");
        TextField avgSale = new TextField();
        avgSale.setText("N/A");
        avgSale.relocate(75,100);
        avgSale.setPrefSize(100, 15);

        //create the lists
        storeList = new ListView<>();
        storeList.relocate(185, 30);
        storeList.setPrefSize(280, 300);
        cartList = new ListView<>();
        cartList.relocate(475, 30);
        cartList.setPrefSize(280, 300);
        popularList = new ListView<>();
        popularList.relocate(10, 165);
        popularList.setPrefSize(165, 165);

        //create the buttons instance
        button = new ElectronicStoreButtonPane();
        button.relocate(0,0);

        getChildren().addAll(label1,label2,label3,label4,label5,label6,label7, numOfSale, revenue, avgSale, button,
                storeList, cartList, popularList);
        setPrefSize(800, 400);
    }
    public ListView<String> getStoreList(){return storeList;}
    public ListView<String> getCartList(){return cartList;}
    public ListView<String> getPopularList(){return popularList;}
    public ElectronicStoreButtonPane getButton(){return button;}
    public void update(ElectronicStore model, int selectProduct){
        String[] storeStock = new String[model.getCurProducts()];
        String []popularStock = new String[3];


        if (selectProduct >= 0){ //selected product index greater than or equal to 0 so it doesn't add item into the cart list
            //check if stock quant of that item is 0 to decrease the stock in store and display onto the listview
            if (model.getStock()[selectProduct].getStockQuantity() == 0){
                model.remove(model.getStock()[selectProduct]);
            }
            cartStock.add(model.getStock()[selectProduct].toString());
            cartList.setItems(FXCollections.observableArrayList(cartStock));
        }


        for (int i = 0; i < model.getCurProducts(); i++){
            storeStock[i] = model.getStock()[i].toString();
        }
        for (int i = 0; i < 3; i++ ){
            popularStock[i] = model.getStock()[i].toString();
        }



        storeList.setItems(FXCollections.observableArrayList(storeStock));
        popularList.setItems(FXCollections.observableArrayList(popularStock));

    }
}
