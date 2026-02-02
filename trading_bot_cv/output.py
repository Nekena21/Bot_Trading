import os
import datetime
import cv2

LOG_PATH = os.path.join(os.path.dirname(__file__), 'logs')


def log_event(message):
    ts = datetime.datetime.now().isoformat()
    line = f"{ts} | {message}"
    print(line)
    try:
        os.makedirs(LOG_PATH, exist_ok=True)
        with open(os.path.join(LOG_PATH, 'signals.log'), 'a', encoding='utf-8') as f:
            f.write(line + "\n")
    except Exception:
        pass


def alert(signal, img=None, sound_path=None):
    """Log, sauvegarde screenshot annoté et joue un son si disponible."""
    log_event(f"SIGNAL {signal}")

    if img is not None:
        try:
            h, w = img.shape[:2]
            cv2.arrowedLine(img, (10, 10), (w // 2, h // 2), (0, 0, 255), 3)
            fname = f"signal_{signal}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            path = os.path.join(LOG_PATH, fname)
            cv2.imwrite(path, img)
            log_event(f"Saved screenshot: {path}")
        except Exception:
            pass

    if sound_path:
        try:
            # import here to avoid hard dependency if user doesn't want sound
            from playsound import playsound

            playsound(sound_path)
        except Exception:
            pass
