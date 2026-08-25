'''Lambda Function: GST Calculator
Create a lambda function gst that returns price after adding 18% GST.
Example:
gst = lambda price: price + (0.18 * price)
print(gst(100)) # should return 118
Create another lambda to compute final price after GST + discount
together.'''

gst = lambda price: price + (0.18 * price)
print(gst(100))

final_price = lambda price, discount: gst(price) - (discount / 100 * gst(price))
print(final_price(100, 10))