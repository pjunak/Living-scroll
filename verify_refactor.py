
import sys
import os
import unittest
import io
from pathlib import Path

# Add project root to path
sys.path.insert(0, os.getcwd())

def run_verification():
    results = []
    
    # Check 1: Pydantic
    try:
        import pydantic
        results.append(f"PASS: Pydantic imported (v{pydantic.VERSION})")
    except ImportError:
        results.append("FAIL: Pydantic not found")
        return "\n".join(results)

    # Check 2: Import new modules
    try:
        from modules.compendium.models import CompendiumRecord
        from modules.compendium.loader import CompendiumLoader
        results.append("PASS: Compendium modules imported")
    except Exception as e:
        results.append(f"FAIL: Import error: {e}")
        return "\n".join(results)

    # Check 3: Run Unit Tests
    results.append("\n--- Unit Test Results ---")
    
    # Capture unittest output
    stream = io.StringIO()
    runner = unittest.TextTestRunner(stream=stream, verbosity=2)
    loader = unittest.TestLoader()
    suite = loader.discover("tests")
    
    result = runner.run(suite)
    
    results.append(stream.getvalue())
    
    if result.wasSuccessful():
        results.append("\nOVERALL: PASS")
    else:
        results.append("\nOVERALL: FAIL")

    return "\n".join(results)

if __name__ == "__main__":
    output = run_verification()
    with open("verification_result.txt", "w") as f:
        f.write(output)
    print("Verification complete.")
