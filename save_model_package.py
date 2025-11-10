# save_model_package.py
import json
import os
from datetime import datetime
import shutil

# Create a package folder
package_name = f"fashion_model_v2_{datetime.now().strftime('%Y%m%d')}"
os.makedirs(package_name, exist_ok=True)

# Copy all files into package
files_to_package = [
    'best_model.h5',           # Model
    'fashion_model.py',         # Code
    'model/class_labels.py',    # Labels
    'model/model_usage.py',     # Usage
    'model_info.json',          # Metadata
    'README.md'                 # Docs
]

print(f"Creating model package: {package_name}")
print("\nFiles included:")
for file in files_to_package:
    if os.path.exists(file):
        dest = os.path.join(package_name, os.path.basename(file))
        shutil.copy2(file, dest)
        print(f"✅ {file} → {dest}")
    else:
        print(f"❌ {file} - missing!")

print(f"\n📦 Package ready: {package_name}/")
print("Upload this entire folder to Google Drive for complete backup!")
