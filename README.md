# VictorySquarePartners
Summer practice at Victory Square Partners 2022

Problems that are not solved yet:
- does not filter the user list, it just selects the desired user
- does not filter the product list, it just selects the desired products (if you select something else (even in read-only), the choice is changed but the quantity and price stay the same). The desired outcome would be to lock the selection, being impossible to change it in the Checkout page.
- order status does not change
- availability should be set to false after a successful order
- order date should be a DateTimeField
- Checkout page should be inaccessible with an empty cart (an error message should be prompted)

Nice to have functionalities:
- order history on profile page
- cancel order functionality along with a notification on email
- send a confirmation email with the order details
- actual payment system (using Stripe or a cryptocurrency API as a proof of concept)
- profile image + default profile image
- default car image
- cancel order + refund functionality
