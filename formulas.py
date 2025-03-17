# תשואה כמה רווח הכסף שהשקעתי השיג
# תשואה זה תמיד במונחי שנה
# כרגע הפונקציות פועלות רק על שנה אחת צריך לשדרג אותם להתאים לכמות הזמן לשנים למשל אם קניתי בית והוא הכפיל את עצמו ב7 שנים כמה תשואה זה

"""
חישוב תשואה ללא מימון, חוק בסיסי לא עושים את זה
"""

# אני קונה ב100 ועושה 10 שח בשנה
def buy_and_make_by_year_yield(price, x_per_year):
    """
    price : int
        the price of the property when u bought it
    x_per_year : int
        how much the property make u each year
    """
    return x_per_year / price * 100

# buy and sell in x months
def buy_and_sell_in_x_month(buy_price, sell_price, months):
    return ((12 * ((sell_price - buy_price) / months)) / buy_price) * 100


def buy_and_rent_yield(price, rent):
    return ((12 * rent) / price) * 100


"""
החלק החשוב חישוב תשואה עם מימון
"""
# חישוב החזר במשכנתא
def calculate_total_payment(principal, annual_interest_rate, years):
    """
    Calculate the monthly payment for a mortgage.

    Parameters:
        principal (float): The loan amount (mortgage principal).
        annual_interest_rate (float): The annual interest rate as a percentage (e.g., 3.5 for 3.5%).
        years (int): The loan term in years.

    Returns:
        int: The monthly payment amount.
    """
    left = years * 12 * principal
    up_side = (annual_interest_rate / 1200) * ((1 + (annual_interest_rate / 1200))**(years*12))
    down_side = ((1 + (annual_interest_rate / 1200))**(years * 12)) - 1
    total = left * (up_side / down_side)
    return round(total)

def calculate_monthly_payment(principal, annual_interest_rate, years):
    return round(calculate_total_payment(principal, annual_interest_rate, years) / (years * 12))

def calculate_monthly_payment_for_ribit(principal, annual_interest_rate):
    return round(((annual_interest_rate / 100) / 12) * principal)

def minuf_yield(hon_azmi, mashcanta, ribit, rent):
    return (12 * (rent - calculate_monthly_payment_for_ribit(mashcanta, ribit))) / hon_azmi * 100


"""
היוון
"""
def hivun(rent, ribit):
    return round((12 * rent) / (ribit / 100))