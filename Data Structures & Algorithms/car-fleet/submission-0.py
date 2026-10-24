class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = zip(position, speed)
        cars = sorted(cars, reverse=True)

        leading_fleet_car_time_to_destination = 0

        fleets = 0

        for position, speed in cars:
            time_to_destination = (target - position) / speed
            
            if time_to_destination <= leading_fleet_car_time_to_destination:
                print()
            else:
                leading_fleet_car_time_to_destination = time_to_destination
                fleets += 1

        return fleets