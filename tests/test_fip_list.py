import pytest
from fip_tools.fip_list import get_all_fips, get_fips_by_status
from fip_tools.fip import Fip

def test_fip_string_representation():
    fip = Fip(42)
    assert str(fip) == "FIP 0042"
    assert repr(fip) == "<Fip(number=42)>"
    fip = Fip(1234)
    assert str(fip) == "FIP 1234"
    assert repr(fip) == "<Fip(number=1234)>"

def test_get_all_fips():
    fips = get_all_fips()
    assert isinstance(fips, list)
    assert all(isinstance(f, Fip) for f in fips)
    assert all(f.number >= 0 for f in fips)
    # Check the list is sorted by FIP number
    numbers = [f.number for f in fips]
    assert numbers == sorted(numbers)
    # Check pathnames are set and valid
    assert all(f.pathname is not None for f in fips)
    assert all(f.pathname.endswith(f"fip-{f.number:04d}.md") for f in fips)
    
    # Check content loading
    for fip in fips:
        content = fip.get_content()
        assert isinstance(content, str)
        assert len(content) > 0
        assert content.startswith('---\n')  # Should have YAML front matter
    
    # Check metadata parsing
    for fip in fips:
        metadata = fip.get_metadata()
        assert isinstance(metadata, dict)
        assert "fip" in metadata
        assert int(metadata["fip"]) == fip.number

def test_get_fips_by_status():
    # Get all FIPs with 'Draft' status (case insensitive)
    draft_fips = get_fips_by_status('Draft')
    draft_fips_lower = get_fips_by_status('draft')
    assert isinstance(draft_fips, list)
    assert isinstance(draft_fips_lower, list) 
    assert all(isinstance(f, Fip) for f in draft_fips)
    assert len(draft_fips) == len(draft_fips_lower)
    assert all(f.get_metadata().get('status', '').lower() == 'draft' for f in draft_fips)
    
    # Check the list is sorted
    numbers = [f.number for f in draft_fips]
    assert numbers == sorted(numbers)
