import java.util.Arrays;
/*
Name: Nick Dang
Date: 23/01/20
Description: Array practice with max(), merge(), average(), areIdentical(), longestIncreasingSequence()
 */

public class ArrayPractice {
    public static void main(String[] args) {
        int[] a = {200,33,4,2,56,49};
        //test max() method
        System.out.println(max(a));

        //test average() method
        int[] b = {1,2,3};
        System.out.println(average(b));

        //test areIdentical() method
        int[] c = {1,2,3};
        int[] d = {1,2,3};
        System.out.println(areIdentical(c,d));

        //test merge() method
        int[] e = {1,2,8,9};
        int[] f = {3,5,6};
        System.out.println(Arrays.toString(merge(e,f)));

        //test longestIncreasingSequence() method
        int[] h = {1,2,3,5,6,7,1,2,3,4,5,6,7,8,1};
        System.out.println(longestIncreasingSequence(h)); //should be 8
    }

    public static int max(int[] arr){
        int biggest = 0;
        for (int j : arr) {
            if (j > biggest) {
                biggest = j;
            }
        }
        return biggest;
    }

    //This method should compute the average/mean of the values contained in the argument array.
    public static double average(int[] arr){
        double sum = 0;
        double average;
        for (int j : arr) {
            sum += j;
        }
        average = sum/arr.length;
        return average;
    }


    //This method should return true if a and b are identical arrays.
    //That is, return true if a and b have the same length and the values at each index are equal
    //Otherwise, the method should return false
    public static boolean areIdentical(int[] a, int[] b){
        if (a.length != b.length){ //check length of 2 arrays
            return false;
        }
        else{
            for (int i = 0; i < a.length; i++){
                if (a[i] != b[i]){ //check value at each index of each array
                    return false;
                }
            }
        }
        return true;
    }

    //The arguments for this method will be two sorted arrays (sorted in increasing order).
    //The method must create and return a new sorted array that contains all the elements from a and b also in increasing order.
    //In other words, you are merging the two sorted lists into a new sorted list.
    //There are many ways to solve this problem, some of which are more efficient than others.
    public static int[] merge(int[] a, int[] b){
        int length = a.length + b.length;
        int[] sorted = new int[length];
        int indexS = 0;
        for (int i = 0; i < a.length; i++){
            sorted[i] = a[i];
            indexS = i;
        }
        indexS += 1; //move the current index of result-array to the next
        for (int j : b) {
            sorted[indexS] = j;
            indexS++;
        }
        Arrays.sort(sorted); //sort the array
        return sorted;
    }

    //This method should return the length of the longest increasing sequence in the argument array.
    //An increasing sequence consists of consecutive numbers that are each larger than the previous.
    //For example, in the array [0, 1, 2, 4, 3, 5, 7], 0-1-2-4 is an increasing sequence of length 4.
    //In the same array, 3-5-7 is an increasing sequence of length 3.
    //Note that 0-1-2-4-3-5-7 is not an increasing sequence as there is a 3 (which is not greater than 4) between 4 and 5.
    public static int longestIncreasingSequence(int[] a){
        int largestSoFar = 1; //variables to keep track of 2 longest sequences.
        int largestSoFar2 = 0;
        for (int i = 0; i < a.length-1; i++){ //{1,2,3,1,4,6,7,8}

            if (a[i] > a[i+1]){
                largestSoFar2 = largestSoFar;
                largestSoFar = 1;
            }
            else{
                largestSoFar++;
            }
        }

        return Math.max(largestSoFar2, largestSoFar);

    }
}
