import java.io.*;

public class StoreTestProgram {
    public static void main(String args[]) {
        Customer[]    result;
        Store         walmart;

        walmart = new Store("Walmart off Innes");
        walmart.addCustomer(new Customer("Amie", 14, 100));
        walmart.addCustomer(new Customer("Brad", 15, 0));
        walmart.addCustomer(new Customer("Cory", 10, 100));
        walmart.addCustomer(new Customer("Dave",  5, 48));
        walmart.addCustomer(new Customer("Earl", 21, 500));
        walmart.addCustomer(new Customer("Flem", 18, 1));
        walmart.addCustomer(new Customer("Gary",  8, 20));
        walmart.addCustomer(new Customer("Hugh", 65, 30));
        walmart.addCustomer(new Customer("Iggy", 43, 74));
        walmart.addCustomer(new Customer("Joan", 55, 32));
        walmart.addCustomer(new Customer("Kyle", 16, 88));
        walmart.addCustomer(new Customer("Smaug", 12, 1000));
        walmart.addCustomer(new Customer("Mary", 17, 6));
        walmart.addCustomer(new Customer("Nick", 13, 2));
        walmart.addCustomer(new Customer("Omar", 18, 24));
        walmart.addCustomer(new Customer("Patt", 24, 45));
        walmart.addCustomer(new Customer("Quin", 42, 355));
        walmart.addCustomer(new Customer("Ruth", 45, 119));
        walmart.addCustomer(new Customer("Snow", 74, 20));
        walmart.addCustomer(new Customer("Tamy", 81, 25));
        walmart.addCustomer(new Customer("Ulsa",  2, 75));
        walmart.addCustomer(new Customer("Vern",  9, 90));
        walmart.addCustomer(new Customer("Will", 9, 220));
        walmart.addCustomer(new Customer("Xeon", 17, 453));
        walmart.addCustomer(new Customer("Ying", 19, 76));
        walmart.addCustomer(new Customer("Zack", 22, 35));

        System.out.println("Here are the customers:\n");
        walmart.listCustomers();

        // Find average Customer age
        System.out.println("\nAverage age of customers: " + walmart.averageCustomerAge());

// Find richest customer
        System.out.println("\nRichest customer is: " + walmart.richestCustomer());

// Find friends for Amie
        System.out.println("\n\nFriends for 18 year old Omar:");
        result = walmart.friendsFor(walmart.getCustomers()[14]);
        for (Customer c:  result) System.out.println(c);

// Find friends for Brad
        System.out.println("\n\nFriends for 14 year old Amie:");
        result = walmart.friendsFor(walmart.getCustomers()[0]);
        for (Customer c:  result) System.out.println(c);

        try {
            DataOutputStream out = new DataOutputStream(new FileOutputStream("store.txt"));
            walmart.saveTo(out);
            out.close();
        } catch (FileNotFoundException e) {
            // Do Nothing
        } catch (IOException e) {
            // Do Nothing
        }
        try {
            DataInputStream in = new DataInputStream(new FileInputStream("store.txt"));
            walmart = Store.readFrom(in);
            in.close();
        } catch (FileNotFoundException e) {
            // Do Nothing
        } catch (IOException e) {
            // Do Nothing
        }
        System.out.println("\n\nHere are the customers from the file's Store object:");
        walmart.listCustomers();
    }



}
