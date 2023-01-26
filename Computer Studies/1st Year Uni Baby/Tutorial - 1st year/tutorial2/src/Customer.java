public class Customer {
    String name;
    int age;
    float money;
    boolean admitted;

    public Customer(String initName) {
        name = initName;
        age = 0;
        money = 0.0f;
        admitted = false;
    }

    public Customer(String initName, int initAge) {
        name = initName;
        age = initAge;
        money = 0.0f;
        admitted = false;
    }

    public Customer(String initName, int initAge, float initMoney) {
        name = initName;
        age = initAge;
        money = initMoney;
        admitted = false;
    }

    public Customer() {
        name = "Unknown";
        age = 0;
        money = 0.0f;
        admitted = false;
    }

    public float computeFee() {
        float basicFee = 12.75f;
        if (age <= 3) {
            basicFee = 0;
        } else if (age >= 65) {
            basicFee = basicFee * 0.5f;
        } else if (age >= 4 && age <= 17) {
            basicFee = 8.50f;
        }
        return basicFee;
    }

    public boolean spend(float amount) {
        if (amount >= 0) {
            if (money >= amount) {
                money -= amount;
                return true;
            }
        }
        return false;
    }

    public boolean  hasMoreMoneyThan(Customer c){
        if (money > c.money){
            return true;
        }
        return false;
    }

    public void payAdmission(){
        if (spend(computeFee())){
            admitted = true;
        }
    }

    public String toString(){
        if (admitted){
            return "Customer " + name +": " + "a " + age + " year old with $" + money + " who has been admitted";
        }
        return "Customer " + name +": " + "a " + age + " year old with $" + money + " who has not been admitted";
    }
}
