class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calculation(self, mass_1, thickness):
        m_calc = self._length * self._width * mass_1 * thickness
        return m_calc

asphalt = Road(20,500)


print(asphalt.mass_calculation(mass_1=25, thickness=5))