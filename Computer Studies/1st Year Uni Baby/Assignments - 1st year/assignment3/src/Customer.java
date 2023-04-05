import java.util.HashMap;
import java.util.Map;


public class Customer implements Comparable<Customer>, java.io.Serializable {
    private final String name;
    private float moneySpent;
    //use hashmap to keep track the items as well as its purchased amount
    private final HashMap<Product,Integer> purchased;
    public Customer (String n){
        moneySpent = 0;
        name = n;
        purchased = new HashMap<>();
    }

    public String toString(){
        return name + " who has spent $" + moneySpent;
    }
    public void purchaseHistory(Product p, int amount){
        if (!purchased.containsKey(p)){
            purchased.put(p,amount);
        }
        else{
            int currentAmount = purchased.get(p);
            purchased.put(p,currentAmount + amount);
        }
        moneySpent += amount * p.getPrice();
    }
    public void printPurchaseHistory(){
        for (Map.Entry<Product,Integer> entry: purchased.entrySet() ){
            System.out.println(entry.getValue() + "x " + entry.getKey());
        }
    }
    public String getName(){return name;}
    public float getMoneySpent(){return moneySpent;}
    public int compareTo(Customer c){
        return (int) (c.getMoneySpent()-this.moneySpent);
    }
}
