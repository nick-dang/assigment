import java.util.Scanner;

public class ElectronicStoreTester {
    public static void main(String[] args) {
        ElectronicStore store = new ElectronicStore("walmart");
        store.printStock();

        Scanner search = new Scanner(System.in);
        String prompt = "";
        
        while (true){
            System.out.print("Enter a search word: ");
            prompt = search.nextLine();
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
