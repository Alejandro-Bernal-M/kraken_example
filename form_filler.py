from playwright.async_api import async_playwright

async def fill_form():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto('https://www.beisbolplay.com/afiliados')
        await page.fill('input[name="your-name"]', 'nombre de ejemplo')
        await page.fill('input[name="your-email"]', 'abernal@rightssentinel.com')
        await page.fill('input[name="tel"]', '1234567890')
        await page.fill('input[name="pais"]', 'Colombia')
        await page.fill('input[name="facebook"]', 'https://www.facebook.com')
        await page.fill('input[name="instagram"]', 'https://www.instagram.com')
        await page.fill('input[name="twitter"]', 'https://www.twitter.com')
        await page.fill('input[name="youtube"]', 'https://www.youtube.com')
        await page.fill('input[name="tiktok"]', 'https://www.tiktok.com')
        await page.locator('span.wpcf7-list-item > label').click(position={'x': 10, 'y': 10})
        await page.wait_for_timeout(9000)  # 5000 milliseconds = 5 seconds

        # await page.click('input[type="submit"][value="Enviar"]')
        await browser.close()



