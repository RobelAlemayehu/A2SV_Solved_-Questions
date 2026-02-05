class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        all_players = set()
        count_losers = defaultdict(int)

        for winner, loser in matches:
            all_players.add(winner)
            all_players.add(loser)
            count_losers[loser] += 1


        zero_lose = []
        one_lose = []

        for player in all_players:
            count = count_losers[player]
            if count == 1:
                one_lose.append(player)
            elif count == 0:
                zero_lose.append(player)
            

        zero_lose.sort()
        one_lose.sort()

        return [zero_lose, one_lose]