class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        left, right = 0, len(skill) - 1

        target = skill[right] + skill[left]
        chemistry = 0

        while left < right:
            if skill[left] + skill[right] == target:
                chemistry += (skill[left] * skill[right])
            else:
                return -1

            left += 1
            right -= 1


        return chemistry

        

