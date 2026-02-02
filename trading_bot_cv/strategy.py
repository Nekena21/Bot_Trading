def reversal_strategy(rsi, macd, candle, price_touch_ma):
    if rsi == "LOW" and macd == "UP" and candle == "GREEN" and price_touch_ma:
        return "CALL"
    if rsi == "HIGH" and macd == "DOWN" and candle == "RED":
        return "PUT"
    return None
