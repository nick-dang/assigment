import java.util.ArrayList;

public class BinaryTree {
    private String	   	data;
    private BinaryTree	leftChild;
    private BinaryTree	rightChild;

    // A constructor that makes a Sentinel node
    public BinaryTree() {
        data = null;
        leftChild = null;
        rightChild = null;
    }

    // This constructor now uses sentinels for terminators instead of null
    public BinaryTree(String d) {
        data = d;
        leftChild = new BinaryTree();
        rightChild = new BinaryTree();
    }

    // This constructor is unchanged
    public BinaryTree(String d, BinaryTree left, BinaryTree right) {
        data = d;
        leftChild = left;
        rightChild = right;
    }

    // Get methods
    public String getData() { return data; }
    public BinaryTree getLeftChild() { return leftChild; }
    public BinaryTree getRightChild() { return rightChild; }

    // Set methods
    public void setData(String d) { data = d; }
    public void setLeftChild(BinaryTree left) { leftChild = left; }
    public void setRightChild(BinaryTree right) { rightChild = right; }

    // Return a list of all data within the leaves of the tree
    public ArrayList<String> leafData()  {
        ArrayList<String>	result = new ArrayList<String>();

        if (data != null) {
            if ((leftChild.data == null) && (rightChild.data == null))
                result.add(data);
            result.addAll(leftChild.leafData());
            result.addAll(rightChild.leafData());
        }
        return result;
    }

    // Determines the height of the tree, which is the number of branches
    // in the path from the root to the deepest leaf.
    public int height()  {
        // Check if this is a sentinel node
        if (data == null)
            return 0;

        return 1 + Math.max(leftChild.height(),
                rightChild.height());
    }

    public boolean isTheSameAs(BinaryTree t) {
        if (data == null && t.getData() == null){ //check the base case of when both trees are empty
            return true;
        }
        if (data != null && t.getData() != null){ //check that the datas aren't null
            //check the data of the trees from the left nodes to the right nodes
            return (data.equalsIgnoreCase(t.getData()) && leftChild.isTheSameAs(t.leftChild) && rightChild.isTheSameAs(t.rightChild));
        }
        return false;
    }

    public boolean contains(String d){
        if (data == null){
            return false;
        }
        if (data.equalsIgnoreCase(d)){
            return true;
        }
        if (leftChild.contains(d)) return true; //check the left nodes first
        return rightChild.contains(d); //if searched string is not found, go through the right nodes
    }
}
