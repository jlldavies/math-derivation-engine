import os
import sys

# make the src/ package importable without installing
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
