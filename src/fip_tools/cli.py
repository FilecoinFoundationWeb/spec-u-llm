import sys
from .fip_list import get_all_fips

def main():
    """Main entry point for specullm CLI"""
    if len(sys.argv) != 2:
        print("Usage: specullm FIP_NUMBER")
        sys.exit(1)
        
    try:
        fip_number = int(sys.argv[1])
    except ValueError:
        print(f"Error: '{sys.argv[1]}' is not a valid FIP number")
        sys.exit(1)
        
    # Find the requested FIP
    fips = get_all_fips()
    matching_fips = [fip for fip in fips if fip.number == fip_number]
    
    if not matching_fips:
        print(f"Error: FIP {fip_number} not found")
        sys.exit(1)
        
    # Print the FIP content
    print(matching_fips[0].get_content())

if __name__ == '__main__':
    main()
