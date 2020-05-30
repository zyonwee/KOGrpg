import random
import KoGDAO.userDAO as u


def Bet(n, choice, bet):
    results = random.randint(1,100)
    if results >= 60:
        u.set_coins(n, bet)
        return f"You placed your bets on {choice} and Won :moneybag: {bet}!"
    if results < 60:
        u.set_coins(n, -bet)
        return f"You placed your bets on {choice} and Lost :moneybag: {bet}!"
