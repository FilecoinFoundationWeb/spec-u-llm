import os
import re
from .fip import Fip

def get_all_fips():
    """
    Returns a sorted list of FIP objects by scanning the FIPs/FIPS directory
    for fip-NNNN.md files.
    
    Returns:
        list[Fip]: Sorted list of FIP objects
    """
    fip_dir = os.path.join("FIPs", "FIPS")
    fips = []
    
    for filename in os.listdir(fip_dir):
        match = re.match(r"fip-(\d{4})\.md", filename)
        if match:
            pathname = os.path.join(fip_dir, filename)
            fips.append(Fip(int(match.group(1)), pathname=pathname))
            
    return sorted(fips, key=lambda f: f.number)
