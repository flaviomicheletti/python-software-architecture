class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __eq__(self, other):
        if isinstance(other, Money):
            return self.amount == other.amount and self.currency == other.currency
        return False

    def __repr__(self):
        return f"Money(amount={self.amount}, currency={self.currency})"
