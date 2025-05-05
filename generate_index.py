import os

def filename_to_title(filename):
    name = filename.replace('.py', '').replace('-', ' ')
    return name.title()

def extract_url(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        first_line = f.readline()
        if first_line.lower().startswith('# url:'):
            return first_line.strip().split(':', 1)[1].strip()
    return None

def main():
    directory = "solutions"
    files = sorted([f for f in os.listdir(directory) if f.endswith(".py")])
    
    print("| # | Problem Name | Solution Link |")
    print("|---|--------------|---------------|")
    
    for idx, file in enumerate(files, 1):
        title = filename_to_title(file)
        print(f"| {idx} | {title}  | [`{file}`](solutions/{file}) |")

if __name__ == "__main__":
    main()
