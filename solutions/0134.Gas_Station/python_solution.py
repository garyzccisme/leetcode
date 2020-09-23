class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        depart, shortage, tank = 0, 0, 0

        for i in range(len(gas)):
            tank += gas[i]
            if cost[i] > tank:
                # Restart at next gas station
                # Record total shortage
                depart = i + 1
                shortage += cost[i] - tank
                tank = 0
            else:
                tank -= cost[i]

        if shortage > tank:
            return -1
        else:
            return depart