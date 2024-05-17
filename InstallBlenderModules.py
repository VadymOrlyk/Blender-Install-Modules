import subprocess
import sys

modules = [
    "Pillow",
    "opencv-python",
    "matplotlib",
    "numpy",
    "packaging"
]

# If you need versions
# modules = [
#     "Pillow>=10.3.0",
#     "opencv-python>=4.8.0.74",
#     "matplotlib>=3.9.0",
#     "numpy>=1.25.2",
#     "packaging>=24.0"
# ]


python_exe = sys.executable
subprocess.run([python_exe, "-m", "ensurepip"], check=True)

subprocess.run([python_exe, "-m", "pip", "install", "--upgrade", "pip"], check=True)

for module in modules:
    subprocess.run([python_exe, "-m", "pip", "install", module], check=True)