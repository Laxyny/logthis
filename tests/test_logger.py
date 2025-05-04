import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from logthis import log_info, log_warn, log_error

def test_log_functions():
    print("Testing log_info:")
    log_info("All systems go.")

    print("Testing log_warn:")
    log_warn("Careful...")

    print("Testing log_error:")
    log_error("Crisis mode engaged.")
    
if __name__ == "__main__":
    test_log_functions()
    print("All tests passed.")