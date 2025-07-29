# Create the ZIP file with all project files
import zipfile
import os

zip_filename = "admybrand-insights-complete.zip"

# Get all files in the project directory
def get_all_files(directory):
    files = []
    for root, dirs, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(root, filename)
            # Skip certain directories
            if any(skip in filepath for skip in ['.git', 'node_modules', '.next', '__pycache__']):
                continue
            files.append(filepath)
    return files

# Create the ZIP file
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    all_files = get_all_files(project_name)
    
    for file_path in all_files:
        # Add file to ZIP with proper path structure
        arcname = file_path
        zipf.write(file_path, arcname)
        
print(f"✅ Created ZIP file: {zip_filename}")
print(f"📦 Total files included: {len(all_files)}")

# List all files in the ZIP for verification
print("\n📁 Project structure in ZIP:")
with zipfile.ZipFile(zip_filename, 'r') as zipf:
    file_list = zipf.namelist()
    file_list.sort()
    
    current_dir = ""
    for file_path in file_list:
        dir_parts = file_path.split('/')
        if len(dir_parts) > 1:
            dir_name = '/'.join(dir_parts[:-1])
            if dir_name != current_dir:
                current_dir = dir_name
                print(f"📂 {dir_name}/")
        
        file_name = dir_parts[-1]
        if file_name:  # Skip directories
            indent = "  " * (len(dir_parts) - 1)
            print(f"{indent}📄 {file_name}")

print(f"\n🎉 Complete project ready for download: {zip_filename}")
print(f"📊 File size: {os.path.getsize(zip_filename) / 1024:.1f} KB")

# Verify ZIP file integrity
try:
    with zipfile.ZipFile(zip_filename, 'r') as zipf:
        bad_files = zipf.testzip()
        if bad_files is None:
            print("✅ ZIP file integrity verified - all files are good!")
        else:
            print(f"❌ Corrupted files found: {bad_files}")
except Exception as e:
    print(f"❌ Error verifying ZIP file: {e}")