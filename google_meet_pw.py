from playwright.sync_api import sync_playwright
import datetime
import time

wktu_meeting = input('kapan meetingnya? ')
while True:
    sekarang = datetime.datetime.now().strftime('%H:%M')
    if sekarang == wktu_meeting:
        with sync_playwright() as playwright:
             #create firefox profile to get cookies of the google acount session, ya gitu dah pokoknya taro sini wkwkwk
            browser = playwright.firefox.launch_persistent_context(headless=False,user_data_dir='PATH FIREFOX PROFILE')
            
            page = browser.pages[0]
            
            page.goto('LINK GUGEL MEET') # insert google meet link here as a string ex: https://meet.google.com/xxx-xxx-xxx
            
            page.click('//span[normalize-space()="Gabung sekarang"]')
            
            input('meetingnya udahan bang silahkan teken enter:   ')
            
            browser.close()
    
        break
    
    