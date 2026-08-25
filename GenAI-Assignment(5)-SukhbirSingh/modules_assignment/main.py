import modules_assignment.math_utils as math_utils
from modules_assignment.math_utils import square
import modules_assignment.string_utils as string_utils
import shop_package.discount as disc
from shop_package.billing import apply_tax, calculate_total


assert math_utils.add(2, 3) == 5
assert math_utils.subtract(5, 2) == 3
assert square(4) == 16
assert string_utils.capitalize_words("hello world") == "Hello World"
assert string_utils.reverse_string("hello") == "olleh"
assert string_utils.word_count("hello world from Python") == 4

print(disc.apply_discount(1000, 10))
print(disc.flat_discount(1000))
print(calculate_total([100, 200, 300]))
print(apply_tax(600))

print("All utility function tests passed.")
