import os
import re

def get_fip_numbers():
    """
    Returns a sorted list of FIP numbers by scanning the FIPs/FIPS directory
    for fip-NNNN.md files.
    
    Returns:
        list[int]: Sorted list of FIP numbers
    """
    fip_dir = os.path.join("FIPs", "FIPS")
    fip_numbers = []
    
    for filename in os.listdir(fip_dir):
        match = re.match(r"fip-(\d{4})\.md", filename)
        if match:
            fip_numbers.append(int(match.group(1)))
            
    return sorted(fip_numbers)
