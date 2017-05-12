package check;

import java.util.Stack;

/**
 * User: fafu
 * Date: 14-12-25
 * Time: 16-26-${SECOND}
 * This class is
 */
public class MaximumArea {
    public int maximalRectangle(char[][] matrix) {
        if (matrix==null||matrix.length==0||matrix[0].length==0)
            return 0;
        int cLen = matrix[0].length;    // column length
        int rLen = matrix.length;       // row length
        // height array
        int[] h = new int[cLen+1];
        h[cLen]=0;
        int max = 0;


        for (int row=0;row<rLen;row++) {
            Stack<Integer> s = new Stack<Integer>();
            for (int i=0;i<cLen+1;i++) {
                if (i<cLen)
                    if(matrix[row][i]=='1')
                        h[i]+=1;
                    else h[i]=0;

                if (s.isEmpty()||h[s.peek()]<=h[i])
                    s.push(i);
                else {
                    while(!s.isEmpty()&&h[i]<h[s.peek()]){
                        int top = s.pop();
                        int area = h[top]*(s.isEmpty()?i:(i-s.peek()-1));
                        if (area>max)
                            max = area;
                    }
                    s.push(i);
                }
            }
        }
        return max;
    }

    public static void main(String[] args){
        MaximumArea m = new MaximumArea();
        char[][] ch =  new char[][]{{'1','0','0','1','1'},{'0','0','1','1','0'},{'1','1','1','1','1'},{'0','1','1','0','1'}};
        m.maximalRectangle(ch);
    }

}
