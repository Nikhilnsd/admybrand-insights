import os
import zipfile
from pathlib import Path

# Create the project structure
project_name = "admybrand-insights-fixed"
base_dir = Path(project_name)

# Create all necessary directories
directories = [
    "app",
    "components", 
    "data",
    "lib",
    "styles"
]

for dir_name in directories:
    (base_dir / dir_name).mkdir(parents=True, exist_ok=True)

print(f"Created project structure: {project_name}")
print("Directories created:")
for dir_name in directories:
    print(f"  - {dir_name}/")