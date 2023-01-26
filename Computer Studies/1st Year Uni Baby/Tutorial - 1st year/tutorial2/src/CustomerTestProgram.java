public class CustomerTestProgram {
    public static void main(String[] args) {
        Customer c = new Customer("bob",27,50);
        Customer c2 = new Customer("john",20);

   
        // c.age = 27;
        // c.money = 50;

       
        // c2.age = 20;


        System.out.println(c.name);
        System.out.println(c.age);
        System.out.println(c.money);

        System.out.println(c2.name);
        System.out.println(c2.age);
        System.out.println(c2.money);

    }
}
