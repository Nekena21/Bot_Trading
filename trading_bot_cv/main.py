import time
import argparse
import datetime
from capture import capture_chart
from vision import preprocess, detect_candle_color
from indicators import rsi_zone
from strategy import reversal_strategy
from filters import cooldown
from output import alert


def main_loop(sleep_interval: float = 5.0, once: bool = False):
    """Main loop.

    sleep_interval: seconds to wait between cycles (default 5s for tests)
    once: if True, run only one cycle then exit
    """
    print("Starting trading_bot_cv (screen-watcher)")
    signals = []  # collect (timestamp, signal)
    try:
        while True:
            img = capture_chart()
            if img is None:
                print("No image captured, retrying in 5s")
                time.sleep(5)
                if once:
                    break
                continue

            edges = preprocess(img)
            candle = detect_candle_color(img)

            # NOTE: placeholders for rsi/macd detection from vision
            # Use simple heuristics / mock values to start
            rsi = rsi_zone(edges)
            macd = "UP"  # placeholder
            price_touch_ma = True  # placeholder

            if not cooldown():
                print("Cooldown active — skipping signal")
            else:
                signal = reversal_strategy(rsi, macd, candle, price_touch_ma)
                if signal:
                    alert(signal, img=img, sound_path=None)
                    signals.append((datetime.datetime.now().isoformat(), signal))

            if once:
                break

            time.sleep(sleep_interval)
    except KeyboardInterrupt:
        print("\nInterrupted by user — shutting down gracefully.")
    finally:
        # Print summary
        print("\n=== Session summary ===")
        print(f"Total signals: {len(signals)}")
        if signals:
            for ts, sig in signals:
                print(f"- {ts} | {sig}")
        print("=== End summary ===")
        return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='trading_bot_cv (screen-watcher)')
    parser.add_argument('--once', action='store_true', help='run a single cycle and exit (useful for tests)')
    parser.add_argument('--sleep', type=float, default=5.0, help='sleep interval between cycles in seconds (default 5)')
    args = parser.parse_args()
    main_loop(sleep_interval=args.sleep, once=args.once)
