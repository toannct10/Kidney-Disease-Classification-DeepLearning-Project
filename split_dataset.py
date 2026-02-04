import zipfile
import os
import shutil

SOURCE_ZIP = r"C:\Users\PC\Downloads\CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone.zip"
EXTRACT_DIR = "tmp_dataset"
OUTPUT_DIR = "CT_KIDNEY_BINARY"
OUTPUT_ZIP = "CT_KIDNEY_BINARY.zip"

KEEP_CLASSES = ["Normal", "Tumor"]

# 1. Unzip dataset gốc
with zipfile.ZipFile(SOURCE_ZIP, 'r') as zip_ref:
    zip_ref.extractall(EXTRACT_DIR)

# 2. Tìm thư mục dataset gốc (tránh bị lồng folder)
root_folder = os.listdir(EXTRACT_DIR)[0]
root_path = os.path.join(EXTRACT_DIR, root_folder)

# 3. Tạo dataset mới chỉ chứa 2 class
os.makedirs(OUTPUT_DIR, exist_ok=True)

for cls in KEEP_CLASSES:
    src = os.path.join(root_path, cls)
    dst = os.path.join(OUTPUT_DIR, cls)
    shutil.copytree(src, dst)

# 4. Zip dataset mới
shutil.make_archive("CT_KIDNEY_BINARY", "zip", OUTPUT_DIR)

# 5. Cleanup (tuỳ thích)
shutil.rmtree(EXTRACT_DIR)
shutil.rmtree(OUTPUT_DIR)

print("✅ Đã tạo CT_KIDNEY_BINARY.zip (Normal vs Tumor)")
