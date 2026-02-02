def rsi_zone(rsi_img):
    # mila découpage RSI zone
    # heuristic simple
    if rsi_img.mean() < 80:
        return "LOW"
    elif rsi_img.mean() > 170:
        return "HIGH"
    else:
        return "MID"
