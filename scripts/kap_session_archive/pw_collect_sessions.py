#!/usr/bin/env python3
"""
Playwright script to collect ALL Manus session UIDs from the sidebar.
Uses the existing Chromium profile (with Manus session cookies).
"""
import json
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

OUTPUT = "/tmp/manus_all_sessions.json"
PROFILE = "/home/ubuntu/.config/chromium"

def collect_sessions():
    sessions = {}
    
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir=PROFILE,
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )
        
        page = browser.pages[0] if browser.pages else browser.new_page()
        
        print("Navigating to Manus...")
        page.goto("https://manus.im/app", wait_until="networkidle", timeout=30000)
        time.sleep(3)
        
        # Check if logged in
        title = page.title()
        print(f"Page title: {title}")
        
        url = page.url
        print(f"Current URL: {url}")
        
        # Try to find sidebar items
        page.wait_for_selector('[role="button"]', timeout=10000)
        
        # Scroll sidebar to load all sessions
        print("Scrolling sidebar to load all sessions...")
        
        prev_count = 0
        scroll_attempts = 0
        max_scrolls = 50
        
        while scroll_attempts < max_scrolls:
            # Click each unvisited session button to get its UID
            buttons = page.query_selector_all('[role="button"]')
            
            for btn in buttons:
                text = btn.inner_text().strip()
                if len(text) > 5 and text not in sessions:
                    try:
                        btn.click()
                        time.sleep(0.5)
                        current_url = page.url
                        if "/app/" in current_url:
                            uid = current_url.split("/app/")[-1].split("/")[0]
                            if len(uid) > 10:  # valid UID
                                sessions[uid] = text
                                print(f"  [{len(sessions)}] {uid[:12]}... → {text[:60]}")
                    except Exception as e:
                        pass
            
            # Scroll the sidebar container
            try:
                page.evaluate("""
                    const sidebar = document.querySelector('nav') || 
                                   document.querySelector('[class*="sidebar"]') ||
                                   document.querySelector('[class*="task-list"]');
                    if (sidebar) sidebar.scrollBy(0, 500);
                    else window.scrollBy(0, 500);
                """)
            except:
                pass
            
            time.sleep(1)
            
            new_count = len(sessions)
            if new_count == prev_count:
                scroll_attempts += 1
            else:
                scroll_attempts = 0
                prev_count = new_count
            
            print(f"  Total collected: {new_count} | Scroll attempts without new: {scroll_attempts}")
        
        browser.close()
    
    return sessions

if __name__ == "__main__":
    print("Starting Playwright session collection...")
    sessions = collect_sessions()
    
    # Save results
    with open(OUTPUT, "w") as f:
        json.dump(sessions, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Done! {len(sessions)} sessions collected → {OUTPUT}")
    
    # Show summary
    archived = {k: v for k, v in sessions.items() if v.startswith("[✓]")}
    unarchived = {k: v for k, v in sessions.items() if not v.startswith("[✓]")}
    print(f"  Already archived [✓]: {len(archived)}")
    print(f"  To process: {len(unarchived)}")
    print("\nUnarchived sessions:")
    for uid, title in unarchived.items():
        print(f"  {uid} → {title[:70]}")
