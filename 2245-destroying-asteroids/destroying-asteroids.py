class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort(reverse=True)
        temp = []

        for asteroid in asteroids:
            if mass >= asteroid:
                mass += asteroid
            else:
                temp.append(asteroid)
            

        temp.sort()

        for asteroid in temp:
            if mass >= asteroid:
                mass += asteroid
            else:
                return(False)
                
        else:
            return(True)
