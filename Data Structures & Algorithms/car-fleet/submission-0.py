class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        # combine 2 arrs 
        for idx, pos in enumerate(position):
            cars.append({ "pos": pos, "speed": speed[idx]})
        # sort by position
        cars.sort(key = lambda x: x["pos"], reverse = True)

        stack = [] # represents how many fleets we've found
        for cur_car in cars:
            # calculate eta of cur car
            cur_eta = (target - cur_car["pos"]) / cur_car["speed"]
            # top of stack is eta of cur fleet we are considering. if cur_car joins cur fleet, then
            # we don't have to do anything. if it doesn't join cur fleet, then we start new fleet by
            # adding to the stack, & that new fleet becomes the cur fleet
            fleet_eta = stack[-1] if stack else 0
            if cur_eta > fleet_eta:
                stack.append(cur_eta)

        return len(stack)