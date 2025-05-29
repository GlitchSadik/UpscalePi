import subprocess
import sys

def run_script(script_path):
    print(f"Running {script_path} ...")
    result = subprocess.run(['python', script_path], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"Error in {script_path}:\n{result.stderr}")
        sys.exit(1)  

def main():
    scripts_in_order = [
        'scripts/load_docs.py',
        'scripts/chunk_docs.py',
        'scripts/embed_docs.py',
        'scripts/query_agent.py'  
    ]

    for script in scripts_in_order:
        run_script(script)

if __name__ == "__main__":
    main()
