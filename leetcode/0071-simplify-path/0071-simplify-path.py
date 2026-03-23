class Solution:
    def simplifyPath(self, path: str) -> str:

        # if there is double slash replace it with single slash
        # single period  is current directory
        # double period is previous directory
        # anything come between single slash is a file name
        #  path starts with slash and can not end with slash 
        stack = []

        paths = path.split("/")

        print(paths)

        for p in paths:
            if p == "." or p == '':
                continue
            elif p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)

        return "/" + "/".join(stack)
            