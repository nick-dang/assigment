//Class representing an electronic store
//Has an array of products that represent the items the store can sell
import java.io.*;
import java.util.*;

public class ElectronicStore implements java.io.Serializable{

  private String name;
  private ArrayList<Product> stock; //Array to hold all products
  private ArrayList<Customer> customers;
  private double revenue;
  
  public ElectronicStore(String initName){
    revenue = 0.0;
    name = initName;
    stock = new ArrayList<>();
    customers = new ArrayList<>();
  }
  
  public String getName(){
    return name;
  }
  
  //Adds a product and returns true if there is space in the array
  //Returns false otherwise
  public boolean addProduct(Product newProduct){
    if (!stock.contains(newProduct)){
      stock.add(newProduct);
      return true;
    }

    return false;
  }

  public boolean registerCustomer (Customer c){
    for (Customer cus: customers){
      if (cus.getName().equalsIgnoreCase(c.getName())){
        return false;
      }
    }
    customers.add(c);
    return true;
  }
  public List<Customer> getCustomers(){
    return customers;
  }
  public List<Product>  searchProducts(String x){
    ArrayList<Product> searchedList = new ArrayList<>();
    for (Product p: stock){
      if (p.toString().toUpperCase().contains(x.toUpperCase())){
        searchedList.add(p);
      }
    }
    return searchedList;
  }
  public List<Product> searchProducts(String x, double minPrice, double maxPrice){
    ArrayList<Product> searchedList = new ArrayList<>();

    for (Product p: stock){
      if (p.toString().toUpperCase().contains(x.toUpperCase())){ //make sure that the searched product matched
        if (p.getPrice()>= minPrice && p.getPrice() <= maxPrice){ //compare product's price with minPrice & maxPrice
          searchedList.add(p); //add into searched list if conditions are met
        }else if(p.getPrice()>= minPrice && maxPrice < 0){
          searchedList.add(p);
        }else if(p.getPrice()<= maxPrice && minPrice < 0){
          searchedList.add(p);
        }
      }
    }
    return searchedList;
  }
  public boolean addStock(Product p, int amount){
    for (Product pro: stock) {
      if (pro.equals(p)){
        p.setStockQuantity(amount);
        return true;
      }
    }
    return false;
  }
  public boolean sellProduct(Product p, Customer c, int amount){
    if (stock.contains(p) && customers.contains(c) && p.getStockQuantity() >= amount){
      revenue += p.sellUnits(amount);
      c.purchaseHistory(p, amount);
      return true;
    }
    return false;
  }
  public List<Customer> getTopXCustomers(int x){
    ArrayList<Customer> customerList = new ArrayList<>();
    Collections.sort(customers);
    if (x <= 0){
      return customerList;
    }else if(x > customers.size()){
      return customers;
    } else {
        for (Customer c: customers){
          if (x > 0){
            customerList.add(c);
          }
          x--;
        }
    }
    return customerList;
  }
  public boolean saveToFile(String filename){
    try{
      ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(filename));
      out.writeObject(this);
      out.close();
      return true;
    }catch (IOException e){
      System.out.println("Error: Cannot write to file");
      return false;
    }
  }

  public static ElectronicStore loadFromFile (String filename){
    try{
      ElectronicStore store;
      ObjectInputStream in = new ObjectInputStream(new FileInputStream(filename));
      store = (ElectronicStore) in.readObject();
      in.close();
      return store;

    }catch(IOException e){
      System.out.println("Error: Cannot found file to read");
    } catch (ClassNotFoundException e) {
      System.out.println("Error: Object's class doesn't match");
    }
    return null;
  }
} 