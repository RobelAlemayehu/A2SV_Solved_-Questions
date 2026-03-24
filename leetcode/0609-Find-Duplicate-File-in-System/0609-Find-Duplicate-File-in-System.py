class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        d = defaultdict(list)

        for path in paths:
            component = path.split()
            directory = component[0]

            for files in component[1:]:
                par = files.find('(')

                filename = files[:par]
                content = files[par + 1: -1]

                full_path = f"{directory}/{filename}"

                d[content].append(full_path)


        return [path for path in d.values() if len(path) > 1]