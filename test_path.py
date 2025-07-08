import os

file_path = r"C:\Users\jps25\OneDrive\Desktop\Documents\Langraph\AI Agents\RAG Agent\Stock_Market_Performance_2024.pdf"

# Check if file exists
if os.path.exists(file_path):
    print("File exists")

# Get the absolute path
abs_path = os.path.abspath(file_path)

# Join paths
joined_path = os.path.join("folder", "subfolder", "file.txt")
print(abs_path)
print(joined_path)