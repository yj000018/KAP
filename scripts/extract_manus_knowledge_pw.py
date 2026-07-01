"""
WP2-M8C — Manus Personalization Knowledge Extraction via Playwright
Extracts all Knowledge items from Manus Settings > Personalization > Knowledge
Uses existing browser session cookies for authentication
"""
import asyncio
import json
import os
import re
from pathlib import Path
from playwright.async_api import async_playwright

OUTPUT_DIR = Path("/home/ubuntu/KAP/02_Source_Acquisition/WP2-M8C_Manus_Knowledge_Playwright")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Get cookies from the sandbox browser (Chromium user data)
COOKIE_FILE = "/home/ubuntu/.config/chromium/Default/Cookies"

async def extract_knowledge():
    async with async_playwright() as p:
        # Launch browser with existing user data to reuse session
        browser = await p.chromium.launch_persistent_context(
            user_data_dir="/home/ubuntu/.config/chromium",
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )
        
        page = browser.pages[0] if browser.pages else await browser.new_page()
        
        print("Navigating to Manus app...")
        await page.goto("https://manus.im/app", wait_until="networkidle", timeout=30000)
        await page.wait_for_timeout(3000)
        
        # Check if logged in
        title = await page.title()
        print(f"Page title: {title}")
        
        # Take screenshot
        await page.screenshot(path=str(OUTPUT_DIR / "01_manus_app_loaded.png"))
        
        # Find and click the user avatar at bottom-left
        # The avatar is at approximately y=750 in the sidebar
        print("Looking for user profile button...")
        
        # Try clicking on the Yannick Jolliet element
        try:
            # Find element by evaluating DOM
            avatar_found = await page.evaluate("""
                () => {
                    const all = Array.from(document.querySelectorAll('*'));
                    const yannick = all.find(el => 
                        el.children.length === 0 && 
                        el.textContent.trim() === 'Yannick Jolliet'
                    );
                    if (yannick) {
                        const r = yannick.getBoundingClientRect();
                        return {found: true, x: r.x + r.width/2, y: r.y + r.height/2};
                    }
                    // Try parent with Yannick text
                    const parent = all.find(el => 
                        el.textContent.includes('Yannick Jolliet') && 
                        el.getBoundingClientRect().height < 60 &&
                        el.getBoundingClientRect().y > 600
                    );
                    if (parent) {
                        const r = parent.getBoundingClientRect();
                        return {found: true, x: r.x + r.width/2, y: r.y + r.height/2};
                    }
                    return {found: false};
                }
            """)
            
            print(f"Avatar search result: {avatar_found}")
            
            if avatar_found.get('found'):
                await page.mouse.click(avatar_found['x'], avatar_found['y'])
                await page.wait_for_timeout(2000)
                await page.screenshot(path=str(OUTPUT_DIR / "02_after_avatar_click.png"))
                print("Clicked avatar")
            else:
                # Try coordinate-based click at bottom of sidebar
                await page.mouse.click(100, 750)
                await page.wait_for_timeout(2000)
                await page.screenshot(path=str(OUTPUT_DIR / "02_after_coord_click.png"))
                print("Clicked at coordinates 100,750")
        except Exception as e:
            print(f"Avatar click error: {e}")
        
        # Look for Personalization menu item
        print("Looking for Personalization menu...")
        try:
            # Try clicking Personalization
            personalization = await page.query_selector('text=Personalization')
            if personalization:
                await personalization.click()
                await page.wait_for_timeout(2000)
                await page.screenshot(path=str(OUTPUT_DIR / "03_personalization_opened.png"))
                print("Clicked Personalization")
            else:
                print("Personalization not found, checking current state")
                content = await page.content()
                if 'Personalization' in content:
                    print("Personalization text exists in DOM")
                    await page.evaluate("document.querySelector('[data-testid=\"personalization\"]')?.click()")
        except Exception as e:
            print(f"Personalization click error: {e}")
        
        # Look for Knowledge tab
        print("Looking for Knowledge tab...")
        try:
            knowledge_tab = await page.query_selector('text=Knowledge')
            if knowledge_tab:
                await knowledge_tab.click()
                await page.wait_for_timeout(2000)
                await page.screenshot(path=str(OUTPUT_DIR / "04_knowledge_tab.png"))
                print("Clicked Knowledge tab")
        except Exception as e:
            print(f"Knowledge tab error: {e}")
        
        # Extract all knowledge items
        print("Extracting knowledge items...")
        items = []
        
        # Scroll and collect all items
        for scroll_n in range(10):
            current_items = await page.evaluate("""
                () => {
                    // Look for knowledge item cards
                    const items = [];
                    
                    // Try various selectors for knowledge items
                    const selectors = [
                        '[class*="knowledge"]',
                        '[class*="memory"]',
                        '[class*="card"]',
                        '[class*="item"]'
                    ];
                    
                    for (const sel of selectors) {
                        const els = document.querySelectorAll(sel);
                        for (const el of els) {
                            const text = el.textContent.trim();
                            if (text.length > 20 && text.length < 5000 && 
                                !text.includes('New task') && !text.includes('Library')) {
                                items.push({
                                    selector: sel,
                                    text: text.substring(0, 500),
                                    y: el.getBoundingClientRect().y
                                });
                            }
                        }
                    }
                    return items;
                }
            """)
            
            if current_items:
                items.extend(current_items)
                print(f"Scroll {scroll_n}: found {len(current_items)} items")
            
            # Scroll down
            await page.evaluate("window.scrollBy(0, 400)")
            await page.wait_for_timeout(500)
        
        # Get full page content
        full_content = await page.content()
        
        # Save raw HTML
        with open(OUTPUT_DIR / "raw_page.html", "w") as f:
            f.write(full_content)
        
        # Save items
        with open(OUTPUT_DIR / "knowledge_items_raw.json", "w") as f:
            json.dump(items, f, indent=2, ensure_ascii=False)
        
        print(f"Total items found: {len(items)}")
        
        # Final screenshot
        await page.screenshot(path=str(OUTPUT_DIR / "05_final_state.png"), full_page=True)
        
        await browser.close()
        return items

if __name__ == "__main__":
    items = asyncio.run(extract_knowledge())
    print(f"Extraction complete. {len(items)} items saved to {OUTPUT_DIR}")
