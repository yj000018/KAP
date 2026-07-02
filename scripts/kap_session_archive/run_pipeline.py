import os
import sys
import subprocess
import time

def run_step(script_name, uid):
    print(f"\n--- Running {script_name} for {uid} ---")
    script_path = os.path.join(os.path.dirname(__file__), script_name)
    result = subprocess.run([sys.executable, script_path, uid], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"Error running {script_name}:")
        print(result.stderr)
        return False
    return True

def process_session(uid):
    print(f"\n{'='*50}\nProcessing Session: {uid}\n{'='*50}")
    
    # Skip deduplication check for testing
    
    if not run_step("01_collect_session.py", uid):
        return False
        
    if not run_step("02_generate_card.py", uid):
        return False
        
    if not run_step("03_save_to_kap_git.py", uid):
        return False
        
    if not run_step("04_mark_archived_in_manus.py", uid):
        print("Warning: Failed to mark as archived in Manus")
        
    # Git commit
    print("\n--- Committing to Git ---")
    os.chdir("/home/ubuntu/KAP")
    subprocess.run(["git", "add", f"03_Archived_Sessions/raw_json/{uid}_verbatim.json", f"03_Archived_Sessions/raw_json/{uid}_card.json"])
    subprocess.run(["git", "add", "03_Archived_Sessions/"])
    subprocess.run(["git", "commit", "-m", f"chore(archive): add session card for {uid}"])
    subprocess.run(["git", "push"])
        
    print(f"✓ Successfully processed {uid}")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_pipeline.py <uid1> [uid2] ...")
        sys.exit(1)
        
    uids = sys.argv[1:]
    for uid in uids:
        process_session(uid)
        time.sleep(2)
