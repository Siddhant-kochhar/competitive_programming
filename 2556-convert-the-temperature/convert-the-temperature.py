class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        res = []
        kelvin = celsius + 273.15
        res.append(kelvin)
        fahrenheit = celsius * 1.80 + 32
        res.append(fahrenheit)
        return res