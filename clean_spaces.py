import os

def clean_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Remove empty lines from the beginning
        while lines and not lines[0].strip():
            lines.pop(0)
            
        # Ensure there's exactly one blank line between imports and code
        content = ''.join(lines).strip() + '\n'
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Cleaned: {file_path}")
    except Exception as e:
        print(f"Error cleaning {file_path}: {str(e)}")

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                clean_file(file_path)

if __name__ == "__main__":
    process_directory('LearningBots') 