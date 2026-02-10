from collections import Counter
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = Counter()

        for entry in cpdomains:
            count, domain = entry.split()

            count = int(count)

            part = domain.split('.')

            for i in range(len(part)):
                sub = ".".join(part[i:])

                counts[sub] += count


        return [f"{c} {d}" for d, c in counts.items()]