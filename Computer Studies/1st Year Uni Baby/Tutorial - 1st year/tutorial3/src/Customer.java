public class Customer {
    private String name;
    private int age;
    private float money;
    private int rewardsId;

    public Customer(String n, int a, float m) {
        name = n;
        age = a;
        money = m;
        rewardsId = -1;
    }

    public String toString() {
        return "Customer " + name + ": a " + age + " year old with $" + money;
    }

    public String getName() { return name; }
    public int getAge() { return age; }
    public int getRewardsld() { return rewardsId; }
    public void setRewardsld(int r ){ rewardsId = r;}

    public boolean hasMoreMoneyThan (Customer c){
        if (money > c.money){
            return true;
        }
        return false;
    }
}
