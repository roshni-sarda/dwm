import java.util.*;
import java.lang.*;

class kMeans {
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter the size of dataset: ");
        int n = scan.nextInt();
        int data[] = new int[n];
        System.out.println("Enter the dataset: ");
        for(int i=0; i<n; i++){
            data[i] = scan.nextInt();
        }
        double m1 = (double)data[0];
        double m2 = (double)data[n-3];
        int cluster[][] = new int[2][n];
        int x,y;
        double oMean1, oMean2;
        do {
            x=0;
            y=0;
           for(int i=0; i<n; i++){
                if(Math.abs(data[i]-m1) <= Math.abs(data[i]-m2) ){
                    cluster[0][x] = data[i];
                    x++;
                }else{
                    cluster[1][y] = data[i];
                    y++;
                }
            } 
            double sum1 = 0.0, sum2 = 0.0;
            oMean1 = m1;
            oMean2 = m2;
           for(int i=0; i<x; i++){
            sum1 = sum1 + cluster[0][i];
           }
           for(int i=0; i<y; i++){
            sum2 = sum2 + cluster[1][i];
           }
           m1 = sum1/x;
           m2 = sum2/y;
        } while (m1 != oMean1 && m2 != oMean2);
        System.out.println("Cluster 1: ");
        for(int i=0; i<x; i++){
            System.out.print(cluster[0][i] + " ");
        }
        System.out.println();
        System.out.println("mean1 : "+ m1);
        System.out.println("Cluster 2: ");
        for(int i=0; i<y; i++){
            System.out.print(cluster[1][i] + " ");
        }
        System.out.println();
        System.out.println("mean2 : "+ m2);
        scan.close();
    }
}