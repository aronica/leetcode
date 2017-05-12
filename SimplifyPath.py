__author__ = 'fafu'

class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        if path=="/../" or path == "/.." or path=="/.":
            return "/"
        if path[0]!='/':
            return None
        stack = list([])
        index = 0
        path = path.rstrip("/")
        while index<len(path):
            p = path.find('/',index+1)
            if p == -1:
                val = path[index+1:]
                if val == ".":
                    break
                elif val == "..":
                    if len(stack)>0:
                        stack.pop()
                    break
                else:
                    stack.append(path[index+1:])
                    break
            if path[index:p]=="/":
                index +=1
            elif path[index:p]=="/.":
                index = p
            elif path[index:p]=="/..":
                if len(stack)>0:
                    stack.pop()
                    index = p
                else:
                    index = p
            else:
                stack.append(path[index+1:p])
                index = p
        if len(stack)>1:
            return '/'+"/".join(stack)
        return "/"
if __name__=="__main__":
    s = Solution()
    st = "/a/./b/../../c/"
    print st,s.simplifyPath(st)
    st = "/..."
    print st,s.simplifyPath(st)
    st = "/a/b/c/d"
    print st,s.simplifyPath(st)
    st = "/a/b/.///c"
    print st,s.simplifyPath(st)
    st = "/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///"
    print st,s.simplifyPath(st)


