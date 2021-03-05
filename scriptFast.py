import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser(
    soup_config={'features': 'lxml'},
    raise_on_404=True,
    user_agent='MyBot/0.1: mysite.example.com/bot_info',
)

browser.open("https://www.walmart.ca/sign-in?from=%2Fen")

userform = browser.select_form("#username")
