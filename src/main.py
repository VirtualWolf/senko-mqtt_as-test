import config
import update_from_github

c = config.read_configuration()

OTA = update_from_github.UpdateFromGitHub(
  username="VirtualWolf", repository="senko-mqtt_as-test", working_dir="src"
)

OTA.update()
