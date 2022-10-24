class OutOfStockException(Exception):
    """Raised when something is out of stock"""
    # Custom error message for this Exception - Kshitij Aji (ka598, Oct 23, 2022)
    error_message = "Sorry, this item is out of stock!"
    pass


class NeedsCleaningException(Exception):
    """Raised when the icecream machine needs cleaning"""
    # Custom error message for this Exception - Kshitij Aji (ka598, Oct 23, 2022)
    error_message = "The Machine needs to be cleaned. Please try again."
    pass


class InvalidChoiceException(Exception):
    """Raised when an invalid choice is picked"""
    # Custom error message for this Exception - Kshitij Aji (ka598, Oct 23, 2022)
    error_message = "Please select a valid choice."
    pass


class ExceededRemainingChoicesException(Exception):
    """Raised when there are too many scoops of icecream"""
    # Custom error message for this Exception - Kshitij Aji (ka598, Oct 23, 2022)
    error_message = "Only a maximum of 3 flavors or 3 toppings can be chosen."
    pass


class InvalidPaymentException(Exception):
    """Raised when an invalid payment amount is given"""
    # Custom error message for this Exception - Kshitij Aji (ka598, Oct 23, 2022)
    error_message = "Please pay the exact amount shown on the screen. "
    pass
