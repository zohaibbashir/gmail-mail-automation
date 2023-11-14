from playwright.sync_api import sync_playwright
import argparse
import getpass
import os


def main():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)

        page = browser.new_page()

        page.goto("https://www.google.com/gmail/about/", timeout=9000)
        page.wait_for_timeout(1000)
        # print(email,recipient,email_cc,email_bcc,email_text)
        # print(email_subject,password)
        signin_xpath='//div[@class="header__aside__buttons"]//a[2]'
        signin_link = page.locator(signin_xpath)
        # print(more_locations_link)
        if signin_link:
            signin_link.click()
            page.wait_for_timeout(1000)
            # print(email)
            page.locator('//input[@type="email"]').fill(email)
            page.wait_for_timeout(3000)

            page.keyboard.press("Enter")
            page.wait_for_timeout(4000)

            page.locator('//input[@type="password"]').fill(password)
            page.wait_for_timeout(2000)

            page.keyboard.press("Enter")
            page.wait_for_timeout(2000)

            page.wait_for_timeout(1000)
            compose_xpath='//div[@class="T-I T-I-KE L3"]'
            compose_button=page.locator(compose_xpath)
            if compose_button:
                compose_button.click()
                page.wait_for_timeout(1000)

                cc_xpath='//span[@class="aB gQ pE"]'
                bcc_xpath='//span[@class="aB  gQ pB"]'
                cc_link=page.locator(cc_xpath)
                bcc_link=page.locator(bcc_xpath)
                cc_link.click()
                bcc_link.click()


                
                page.locator('//div[@name="to"]//input').fill(recipient)
                is_pop_up = page.locator('//div[@name="to"]//input').evaluate('(element) => element.getAttribute("aria-expanded")')
                if is_pop_up:
                    page.keyboard.press("Enter")
                page.wait_for_timeout(1000)
                

                page.locator('//div[@name="cc"]//input').fill(email_cc)
                page.wait_for_timeout(1000)
                page.locator('//div[@name="bcc"]//input').fill(email_bcc)
                page.locator('//input[@name="subjectbox"]').fill(email_subject)
                page.locator('//div[@class="Am Al editable LW-avf tS-tW"]').fill(email_text)
                page.wait_for_timeout(1000)

                send_xpath='//div[@class="T-I J-J5-Ji aoO v7 T-I-atl L3"]'
                send_link=page.locator(send_xpath)
                send_link.click()
                page.wait_for_timeout(4000)
        browser.close()
        os.system('cls')
        print("Your Mail has been sent successfully\n")
                

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--email", type=str)
    parser.add_argument("-p", "--pswd", type=str)
    parser.add_argument("-to", "--to", type=str)
    parser.add_argument("-cc", "--cc", type=str)
    parser.add_argument("-bcc", "--bcc", type=str)
    parser.add_argument("-S","--subject", type=str)
    parser.add_argument("-T", "--text", type=str)
    
    email=recipient=email_cc=email_bcc=email_text=email_subject=""
    args = parser.parse_args()

    if args.email:
        email=args.email

    if args.pswd:
        password=args.pswd
    else:
        password = getpass.getpass('Enter Password: ')

    if args.to:
        recipient = args.to
    if args.cc:
        email_cc = args.cc
    if args.bcc:
        email_bcc = args.bcc
    if args.subject:
        email_subject = args.subject
    if args.text:
        email_text = args.text


    main()
       
