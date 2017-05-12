package check;

import java.util.*;

/**
 * User: fafu
 * Date: 14-12-30
 * Time: 13-19-${SECOND}
 * This class is
 */
public class NQueue {


    public List<List<String>> solveNQueens(int n) {
        if(n< 4){
            return null;
        }

        List<List<Integer>> result =new ArrayList<List<Integer>>();
        __calc__(new ArrayList<Integer>(),result, 0, new HashSet<Integer>(),n);
        List<List<String>>newresult =new ArrayList<List<String>>();
        for(List<Integer> i:result){
//        List<List<String> res =
//                Collections.fill();
//        j = 0
//        while j<n:
//        res[j][i[j]] = "Q"
//        j += 1
//        newresult.append(["".join(m) for m in res])
        }
        return newresult;
    }

    public void __calc__(List<Integer> tmp, List<List<Integer>> result, int index, Set se, int n) {
        int lens = tmp.size();
        for (int i = 0; i < n; i++) {
            if (se.contains(i) && (tmp.size() == 0 || Math.abs(tmp.get(tmp.size() - 1) - i) != 1)) {

                tmp.add(i);
                se.add(i);
                if (index + 1 == n)
                    result.add(tmp);
                else {
                    __calc__(tmp, result, index + 1, se, n);
                    se.remove(i);
                }
            }

        }
    }
}