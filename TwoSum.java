package check;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * User: fafu
 * Date: 2015/3/19
 * Time: 14-48-${SECOND}
 * This class is
 */
public class TwoSum {
    public int[] twoSum(int[] numbers, int target) {
        Map<Integer,Integer> map = new HashMap<Integer,Integer>();
        for(int i = 0;i<numbers.length;i++){
            if(map.get(numbers[i])==null){
                map.put(target-numbers[i],i);
            }else{
                return new int[]{map.get(numbers[i])+1,i+1};
            }
        }
        return null;
    }

    public static void main(String[] args){
        TwoSum s = new TwoSum();
        System.out.println(Arrays.toString(s.twoSum(new int[]{3,2,4},6)));
    }
}
