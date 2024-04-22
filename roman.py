r = str(input('Enter your number'))
class py_solution:
    def roman_to_int(self, r):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(r)):
            if i > 0 and rom_val[r[i]] > rom_val[r[i - 1]]:
                int_val += rom_val[r[i]] - 2 * rom_val[r[i - 1]]
            else:
                int_val += rom_val[r[i]]
        return int_val

print(py_solution().roman_to_int(r))


