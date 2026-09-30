class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p,s) for p, s in zip(position, speed)]
        cars.sort(reverse = True) 
        stack = [] 
        for pos, speed in cars: 
            cur_eta = (target - pos) / speed              #calculate current eta
            fleet_eta = stack[-1] if stack else 0  # fleet_eta is top of the stack=previous car 
            if cur_eta > fleet_eta:  
                stack.append(cur_eta) # will store current eta if 
        return len(stack)