import javax.swing.JOptionPane;

public class ElectronicStoreTester {
    public static void main(String[] args) {
        ElectronicStore store = new ElectronicStore("walmart");
        store.printStock();

        
        while (true){
            String prompt = JOptionPane.showInputDialog(null, "Enter a search word");
            if (prompt.equalsIgnoreCase("quit")){
                break;
            }
            if (store.searchStock(prompt)){
                System.out.println("A matching item is contained in the store's stock");
            }
            else{
                System.out.println("No item in the store's stock match that term.");
            }
        }
    }
}
