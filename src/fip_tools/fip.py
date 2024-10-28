class Fip:
    """Represents a Filecoin Improvement Proposal (FIP)"""
    
    def __init__(self, number: int, pathname: str = None):
        """
        Args:
            number (int): The FIP number
            pathname (str, optional): Path to the FIP markdown file
        """
        self.number = number
        self.pathname = pathname
        
    def __str__(self) -> str:
        """Returns the FIP number as a zero-padded string like 'FIP 0000'"""
        return f"FIP {self.number:04d}"
        
    def __repr__(self) -> str:
        """Returns a detailed string representation for debugging"""
        return f"<Fip(number={self.number})>"
