## 134. Gas Station

### Problem Link 
https://leetcode.com/problems/gas-station/

### Note
The solution is a bit of tricky. It defines three variables:

- `depart`: the starting gas station's index.
- `shortage`: the total debt gas.
- `tank`: current gas in tank.

The main process is like a simulation:
- Go loop with `gas` and `cost`.
    - Fill gas to `tank`.
    - If `tank` can't meet the cost, then restart at next gas station, record total gas `shortage`, clear `tank`.
    - Else move on to next gas station.
- If final `tank` can't still meet final `shortage`, then return -1. 
- Else return `depart` as the index of starting gas station's index.
