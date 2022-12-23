import senko
import logger

OTA = senko.Senko(
  user="virtualwolf", repo="senko-mqtt_as-test", files = ["mqtt_as.py"]
)

if OTA.update():
    logger.log("Got new updates")
else:
    logger.log("No new updates")
