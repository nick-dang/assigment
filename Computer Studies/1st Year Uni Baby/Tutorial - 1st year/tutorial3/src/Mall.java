/*Nick Dang
 * 101286968
 * 
 */
public class Mall {
    public static final int MAX_STORES = 100;
    private String name;
    private Store[] stores;
    private int storeCount;

    public Mall(String n) {
        name = n;
        stores = new Store[MAX_STORES];
        storeCount = 0;
    }

    public void addStore(Store s) {
        if (storeCount < MAX_STORES) {
            stores[storeCount++] = s;
        }
    }

    public boolean shoppedAtSameStore(Customer c1, Customer c2){
        for (int i =0; i < storeCount; i++){
            for (int j = 0; j < stores[i].getCustomerCount(); j++){
                if (stores[i].getCustomers()[j].equals(c1)){
                    for (int k = j; k < stores[i].getCustomerCount(); k++){
                        if (stores[i].getCustomers()[k].equals(c2)){ 
                            return true;
                        }
                    }
                }
            }
        }
        return false;
    }
}