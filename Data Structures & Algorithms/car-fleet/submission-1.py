class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arg_sorted = sorted(range(len(position)), key=position.__getitem__, reverse=True)
        last_fleet_time_steps, num_fleets = None, 0
        for i in arg_sorted:
            fleet_time_steps = (target - position[i])/speed[i]
            if last_fleet_time_steps is None:
                last_fleet_time_steps = fleet_time_steps
                num_fleets = 1
            if fleet_time_steps > last_fleet_time_steps:
                num_fleets += 1
                last_fleet_time_steps = fleet_time_steps
        return num_fleets
            
