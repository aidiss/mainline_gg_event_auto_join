"""It will be hard to make this work as a script, as login is required after browser is launched.
Use Jupyter notebook or pure ipython for interactive session."""
from selenium.webdriver import Chrome
import time


def get_current_max() -> int:
    xpath = '//div[@class="matches"]/div/div'
    matches = [x.get_attribute('data-key') 
               for x in driver.find_elements_by_xpath(xpath)]
    matches = [int(x) for x in matches if x]
    current_max = max(matches)
    return current_max

def get_event_page_and_follow(match_id: int, max_tries: int) -> bool:
    xpath = '//div[@data-key="%s"]/div[@class="match animate"]' % match_id
    for _ in range(max_tries):
        driver.refresh()
        results = driver.find_elements_by_xpath(xpath)
        if results:
            match = results[0]
            match.click()
            return True
    return False

def follow_xpath(xpath):
    results = driver.find_elements_by_xpath(xpath)
    submit_button = results[0]
    submit_button.click()

def main():
    global driver
    driver = Chrome()
    driver.get('https://play.mainline.gg/')

    max_tries = 10
    driver.refresh()
    match_id = get_current_max()
    if get_event_page_and_follow(match_id=match_id, max_tries=max_tries):
        follow_xpath('//a[@class="button join-button"]')
        follow_xpath('//div[@id="eventteamselectform-team_id"]')
        follow_xpath('//button[@type="submit"]')

if __name__ == '__main__':
    main()
