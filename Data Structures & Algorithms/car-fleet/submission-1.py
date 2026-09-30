class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p,s) for p, s in zip(position, speed)]
        cars.sort(reverse = True) 
        stack = [] 
        for pos, speed in cars: 
            cur_eta = (target - pos) / speed 
            fleet_eta = stack[-1] if stack else 0
            if cur_eta > fleet_eta:
                stack.append(cur_eta)
        return len(stack)