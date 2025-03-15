class Property():
    """
    A class used to represent a general property

    ...

    Attributes
    ----------
    buying_price : int
        The price to buy the property
    rent : int
        the amount of rent u can get each month

    Methods
    -------
    buy_and_sell_in_x_months(sell_price, months)
        return the yield of the property after sell in x months
    buy_and_make_x_amount_year(amount_per_year)
        return the yield by the amount you make per year (like from rent)
    """
    def __init__(self, buying_price, rent):
        self.buying_price = None
        self.rent = None

    """
    return the yield of the property after sell in x months

    Parameters
    ----------
    sell_price : int
        The price that u sell the property
    months : int
        The number of months that passed from the time of purchase to the time of sale
    """
    """
    return the yield by the amount you make per year (like from rent)

    price : int
        the price of the property when u bought it
    x_per_year : int
        how much the property make u each year
    """
    def buy_and_sell_in_x_months(self, sell_price, months):
        return ((12 * ((sell_price - self.buying_price) / months)) / self.buying_price) * 100

    def buy_and_make_x_amount_year(self, amount_per_year):
        return amount_per_year / self.buying_price * 100

    """
    return the yield of buying and renting a property
    :return: return the yield of buying and renting a property
    """
    def buy_and_rent(self):
        return ((12 * self.rent) / self.buying_price) * 100

    """
    Calculate the monthly payment for a mortgage.

    Parameters:
        principal (float): The loan amount (mortgage principal).
        annual_interest_rate (float): The annual interest rate as a percentage (e.g., 3.5 for 3.5%).
        years (int): The loan term in years.

    Returns:
        int: The monthly payment amount.
    """
    # חישוב החזר במשכנתא
    def calculate_total_payment(self, principal, annual_interest_rate, years):
        left = years * 12 * principal
        up_side = (annual_interest_rate / 1200) * ((1 + (annual_interest_rate / 1200)) ** (years * 12))
        down_side = ((1 + (annual_interest_rate / 1200)) ** (years * 12)) - 1
        total = left * (up_side / down_side)
        return round(total)

    def calculate_monthly_payment(self, principal, annual_interest_rate, years):
        return round(self.calculate_total_payment(principal, annual_interest_rate, years) / (years * 12))

    def calculate_monthly_payment_for_ribit(self, principal, annual_interest_rate):
        return round(((annual_interest_rate / 100) / 12) * principal)

    def minuf_yield(self, hon_azmi, mashcanta, ribit, rent):
        return (12 * (rent - self.calculate_monthly_payment_for_ribit(mashcanta, ribit))) / hon_azmi * 100

    """
    היוון
    """

    def hivun(self, rent, ribit):
        return round((12 * rent) / (ribit / 100))

