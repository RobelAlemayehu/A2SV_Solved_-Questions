class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        dic = {}
        for response in responses:

            _set = set(response)

            for item in _set:
                dic[item] = dic.get(item, 0) + 1


        result = ""
        max_freq = -1

        for response, freq in dic.items():
            if freq > max_freq:
                result = response
                max_freq = freq

            elif freq == max_freq:
                if response < result:
                    result = response

        return result