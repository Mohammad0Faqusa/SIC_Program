import subprocess

source_file = 'sicProgram.txt'
def run_python_files(files):
    for file in files:
        subprocess.run(['python', file])

# Example usage:
files_to_run = ['pass1.py', 'pass2.py']
run_python_files(files_to_run)
