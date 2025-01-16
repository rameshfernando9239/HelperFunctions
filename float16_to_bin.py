import struct
import numpy as np

def float16_to_binary(num):
    """
    Convert a floating point number to its 16-bit (half-precision) binary representation.
    
    Format: 1 bit sign | 5 bits exponent | 10 bits fraction
    
    Parameters:
    num (float): Input floating point number
    
    Returns:
    str: 16-bit binary representation
    """  
    try:
        # Convert float to float16
        f16 = np.float16(num)
        
        # Get the bytes of float16
        bytes_val = f16.tobytes()
        
        # Convert bytes to integer
        int_val = struct.unpack('H', bytes_val)[0]
        
        # Convert to binary and ensure it's 16 bits
        binary = format(int_val, '016b')
        
        # Split the binary string for readability
        sign = binary[0]
        exponent = binary[1:6]
        fraction = binary[6:]
        
        return f"{sign}_{exponent}_{fraction}"
    except (ValueError, OverflowError):
        return "Invalid input or value out of float16 range"