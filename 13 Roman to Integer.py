class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Mapping of Roman numerals to integer values
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0  # Store the final integer value
        prev_value = 0  # Store the previous numeral's value for comparison
        
        # Iterate through the string from right to left
        for char in reversed(s):
            current_value = roman_values[char]  # Get the integer value of the current Roman numeral
            
            # If the current value is smaller than the previous one, subtract it (e.g., IV -> 4)
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            
            prev_value = current_value  # Update the previous value for the next iteration
        
        return total
