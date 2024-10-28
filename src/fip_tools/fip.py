import yaml

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
        self._metadata = None
    
    def get_metadata(self) -> dict:
        """Returns the YAML front matter metadata from the FIP markdown file as a dict.
        
        Returns:
            dict: The parsed YAML metadata
        
        Raises:
            FileNotFoundError: If the FIP file doesn't exist
            ValueError: If the file doesn't contain valid YAML front matter
        """
        if self._metadata is None and self.pathname:
            with open(self.pathname) as f:
                content = f.read()
            
            # Find YAML front matter between --- markers
            if content.startswith('---\n'):
                end = content.find('\n---\n', 4)
                if end != -1:
                    yaml_content = content[4:end]
                    try:
                        self._metadata = yaml.safe_load(yaml_content)
                    except (yaml.YAMLError, ValueError) as e:
                        raise ValueError(f"Invalid YAML front matter in {self.pathname}: {str(e)}")
                else:
                    raise ValueError(f"No closing YAML front matter marker found in {self.pathname}")
            else:
                raise ValueError(f"No YAML front matter found in {self.pathname}")
                
        return self._metadata or {}
        
    def __str__(self) -> str:
        """Returns the FIP number as a zero-padded string like 'FIP 0000'"""
        return f"FIP {self.number:04d}"
        
    def __repr__(self) -> str:
        """Returns a detailed string representation for debugging"""
        return f"<Fip(number={self.number})>"
