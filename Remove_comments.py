class Solution:
    def removeComments(self, source: List[str]) -> List[str]:

        in_block = False

        program = []

        strings = ""

        for line in source:
            i = 0
            
            if not in_block:
                strings = ""

            while i < len(line):
                if line[i:i+2] == "//" and not in_block:
                    break 
                
                elif  line[i:i + 2] == "/*" and not in_block:
                    in_block = True
                    i += 1

                elif  line[i:i + 2] == "*/" and in_block:
                    in_block = False
                    i += 1

                elif not in_block:
                    strings += line[i]

                i += 1



            if not in_block and strings:
                program.append(strings) 


        return program 
                
                

        
