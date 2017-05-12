__author__ = 'fafu'
from Meta import ListNode
class Solution:


    #word ladder2
    def ladderLength2(self, start, end, dict):
        if start == end:
            return [[start]]
        if dict is None:
            return []

        all_chars = map(chr, xrange(ord('a'), ord('z') + 1))
        visited = {}
        dis = {start:1}
        bfs = [ListNode(start), None]
        distance = 2
        # at which distance the following to-be-processed nodes are
        result = []
        found = False
        while len(bfs) > 1:
            node = bfs.pop(0)

            if node is None:
                distance  += 1
                if not found:
                    bfs.append(None)
                    continue
                else:
                    break
            word = node.val

            for i in xrange(len(word)):
                for char in all_chars:
                    new_word = word[:i] + char + word[i + 1:]
                    if new_word == end:
                        result.append(node)
                        if not found:
                            found = True
                        break
                    elif new_word == word:
                        Found = True
                        continue
                    elif new_word in dict and new_word not in visited:
                        newnode = ListNode(new_word)
                        newnode.next = [node]
                        bfs.append(newnode)
                        visited[new_word] = (newnode,distance)
                        if new_word in dis and dis[new_word]<distance-1:
                            continue
                        else:
                            dis[new_word] = distance-1
                    elif new_word in dict and new_word in visited and new_word in dis:
                        if dis[new_word]<distance-1:
                            continue
                        newnode = visited[new_word]
                        if newnode[1] < distance:
                            newnode[0].next.append(node)

        newresult = []

        for i in result:
            self.dfs_wordladder(i,[end],newresult)
        return newresult

    def dfs_wordladder(self,node,result,newresult):
        result.append(node.val)
        leng = len(result)
        if node.next is not None:
            for i in node.next:
                self.dfs_wordladder(i,result,newresult)
                del result[leng:]
        else:
            tmp = [i for i in result]
            tmp.reverse()
            newresult.append(tmp)

    def findLadders(self, start, end, words):
        pathes=[];
        graphNodes={};
        queue=[(start,0,[])];
        minPath=0;
        nodeShortPathCache={};

        while(len(queue)>0):
            node,dis,path=queue.pop(0);

            if(node not in graphNodes):
                graphNodes[node]=[];
                for i in range(len(node)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if(j==node[i]):
                            continue;
                        newNode = node[0:i] + j + node[i + 1:]
                        if(newNode in words):
                            graphNodes[node].append(newNode)

            if(node in nodeShortPathCache):
                if(dis>nodeShortPathCache[node]):
                    continue;
            else:
                nodeShortPathCache[node]=dis;
            if(node==end):
                newpath=list(path);
                newpath.append(node);
                if(minPath==0):
                    minPath=dis;
                if(dis==minPath):
                    pathes.append(newpath);
            else:
                newpath=list(path);
                newpath.append(node);
                for childNode in graphNodes[node]:
                    if(childNode in nodeShortPathCache):
                        if(dis+1>nodeShortPathCache[childNode]):
                            continue;
                    queue.append((childNode,dis+1,newpath));
        return pathes;
