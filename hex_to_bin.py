def hex_to_binary(hex_num):
    """
    Convert a hexadecimal number (as a string) to its binary representation.

    Parameters:
    hex_num (str): The hexadecimal number as a string (e.g., '1A', 'FF').

    Returns:
    str: The binary representation of the number as a string.
    """
    try:
        #If the input is already an integer
        if isinstance(hex_num, int):
            binary_representation = bin(hex_num)[2:]
        #If input is a string
        else:
            hex_str = hex_num.replace('0x', '').replace('0X', '')
            # Convert hex to integer, then to binary, and remove the '0b' prefix
            binary_representation = bin(int(hex_num, 16))[2:]
        return binary_representation
    except (ValueError, AttributeError):
        return "Invalid hexadecimal input"