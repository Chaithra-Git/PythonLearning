def process_value(value):
    try:
        if value < 0:
            raise ValueError("Value must be non-negative.")
    except ValueError as e:
        print("Caught an exception:", e)
        raise  # Re-raises the same exception for higher-level handling

try:
    process_value(-10)
except ValueError as e:
    print("Handled exception in outer block:", e)