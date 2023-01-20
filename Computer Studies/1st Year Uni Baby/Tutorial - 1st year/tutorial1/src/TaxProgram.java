import java.util.Scanner;
/*
Name: Nick Dang
Date: 23/01/20
Description: calculate the user's income, federal tax, provincial tax and total tax based on the dependants
 */
public class TaxProgram {
    public static void main(String[] args) {
        double income, fedTax, provTax;

        int dependents;

        Scanner input = new Scanner(System.in);
        System.out.print("Please enter your taxable income: ");
        income = input.nextDouble();
        System.out.println();
        System.out.print("Please enter your number of dependents: ");
        dependents = input.nextInt();
        System.out.println();
        fedTax = 0.0f;

        if (income <= 29590){
            fedTax = (income*0.17);
        }
        else if (income > 29590.01 & income < 59179.99){
            fedTax = (29590 *0.17 + 0.26*(income - 29590));
        }
        else if (income >= 59180){
            fedTax = (0.17*29590 + 0.26*29590 + 0.29*(income-59180));
        }

        //base of prov tax
        double base = 0.425*fedTax;

        double deduction = 160.50 + 328*dependents;

        if (base < deduction){
            provTax = 0.0;
        }
        else{
            provTax = base - deduction;
        }

        double TotalTax = fedTax + provTax;


        System.out.println("Here is your tax breakdown:\n");
        System.out.println(String.format("%-15s%,10.2f","Income",income));
        System.out.println(String.format("%-20s","Dependants     ") + dependents);
        System.out.println("----------------------------");
        System.out.println(String.format("%-15s%,10.2f","Federal Tax",fedTax));
        System.out.println(String.format("%-15s%,10.2f","Provincial Tax",provTax));
        System.out.println("============================");
        System.out.println(String.format("%-15s%,10.2f","Total Tax",TotalTax));



    }
}
