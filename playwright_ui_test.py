from playwright.sync_api import sync_playwright

# Validate able to open browser to a specific landing page, then close browser
def test_landing_page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=1000) # Launch browser
        page = browser.new_page() # Open new page
        page.goto('https://playwright.dev/python/') # Navigate to site
        browser.close() # Close browser


# The same scenario but capture a screenshot after loading the page
def test_landing_page_screenshot():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=1000)  # Launch browser
        page = browser.new_page()  # Open new page
        page.goto('https://playwright.dev/python/')  # Navigate to site
        page.screenshot(path='example_chromium.png')  # Take screenshot
        browser.close()  # Close browser


# The same scenario but using multiple browsers
def test_landing_page_screenshot_multi_browsers():
    with sync_playwright() as playwright:
        for browser_type in [playwright.chromium, playwright.firefox, playwright.webkit]:  # Loop through different browsers
            browser = browser_type.launch(headless=False, slow_mo=1000) # Launch browser
            page = browser.new_page() # Open new page
            page.goto('https://playwright.dev/python/') # Navigate to site
            page.screenshot(path=f'example_{browser_type.name}.png')  # Save screenshot per browser
            browser.close() # Close browser