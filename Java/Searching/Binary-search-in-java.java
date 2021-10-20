package Arrays;

public class BinarySearch {
    public static int binary(int[] arr,int ele){
        int start=0;
        int end= arr.length-1;

        while(start<=end){
            int mid=start+(end-start)/2;
            if(ele==arr[mid]){
                return mid;
            }
            else if(ele>arr[mid]){
                start=mid+1;
            }
            else{
                end=mid-1;
            }
        }
        return -1;
    }
    public static void main(String[] args) {
        int[] arr={2,3,5,2883,73,38,4,0};
   int ans=binary(arr,4);
        System.out.println(ans);



    }
}
