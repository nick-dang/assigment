/*Nick Dang
 * 101286968
 * 
 */
public class Store {
    public static final int MAX_CUSTOMERS = 500;
    private String name;
    private Customer[] customers;
    private int customerCount;
    private static int LATEST_ID = 100000;

    public Store(String n) {
        name = n;
        customers = new Customer[MAX_CUSTOMERS];
        customerCount = 0;
    }

    public void addCustomer(Customer c) {
        if (customerCount < MAX_CUSTOMERS)
            c.setRewardsld(LATEST_ID++);
            customers[customerCount++] = c;

    }

    public void listCustomers() {
        for (int i = 0; i < customerCount; i++)
            System.out.println(customers[i]);
    }

    public int averageCustomerAge() {
        int sum = 0;
        for (int i = 0; i < customerCount; i++) {
            sum += customers[i].getAge();
        }
        return sum / customerCount;
    }
    
    public Customer richestCustomer() {
        Customer currentCustomer = customers[0];
        for (int i = 0; i < customerCount - 1; i++) {
            if (customers[i].hasMoreMoneyThan(currentCustomer)) {
                currentCustomer = customers[i];
            }
        }
        return currentCustomer;
    }
    
    public Customer[] friendsFor(Customer lonelyCustomer){
        int age = lonelyCustomer.getAge();
        int maxAge = age+3;
        int minAge = age-3;
        int maxFriends = 0;
        Customer[] TempListOfFriends = new Customer[customerCount];
        
        for (int i = 0; i < customerCount; i++){
            if (age == customers[i].getAge() || (maxAge >= customers[i].getAge() && minAge <= customers[i].getAge())){
                if(!customers[i].equals(lonelyCustomer)){ //prevent adding the lonely customer themselves into the array
                    TempListOfFriends[maxFriends] = customers[i];
                    maxFriends++;
                }
            }
        }
        Customer[] listOfFriends = new Customer[maxFriends]; //new array without 'null'
        for (int i = 0; i <maxFriends; i++){
            listOfFriends[i] = TempListOfFriends[i];
        }
        return listOfFriends;
    }

    public Customer[] getCustomers() {
        return customers;
    }

    public int getCustomerCount() {
        return customerCount;
    }

    
}