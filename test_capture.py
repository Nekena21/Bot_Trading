from trading_bot_cv.capture import capture_chart

img = capture_chart()
print('OK' if img is not None else 'NO IMAGE')