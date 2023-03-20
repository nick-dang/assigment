import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;

public class Customer {
    private String      name;
    private int         age; 
    private float       money;
    private int id;

    public Customer(String n, int a, float m) {
        name = n;
        age = a; 
        money = m;
        id = -1;
    }
    
    public void setID(int newID){
      id = newID;
    }

    public String toString() {
        return "Customer " + name + ": a " + age + " year old with $" + money;
    }
    
    public String getName() { return name; }
    public int getAge(){return age;}
    public float getMoney (){return money;}
    public int getId(){return id;}
    
    public boolean hasMoreMoneyThan(Customer c) {
      return money > c.money;
    }

    public void saveTo(DataOutputStream aFile) throws IOException {
        aFile.writeUTF(name);
        aFile.writeInt(age);
        aFile.writeFloat(money);
        aFile.writeInt(id);

    }

    public static Customer readFrom(DataInputStream aFile) throws IOException {
        Customer customer = new Customer(aFile.readUTF(), aFile.readInt(), aFile.readFloat());
        customer.setID(aFile.readInt());
        return customer;
    }
}
