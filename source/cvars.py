GIA_VERSION = "v1.0.0.1236"
"""Constants."""

# Devices
DESKTOP_CN = "Desktop_CN"
DESKTOP_EN = "Desktop_EN"
MOBILE_CN = "Mobile_CN"
MOBILE_EN = "Mobile_EN"
DEVICE = DESKTOP_CN

# Interaction modes
INTERACTION_DESKTOP = "Desktop"
INTERACTION_EMULATOR = "Emulator"
INTERACTION_DESKTOP_BACKGROUND = "DesktopBackground"
INTERACTION_MODE = INTERACTION_DESKTOP # Normal, Adb, Dm
BBG = 100001

# Angle modes
ANGLE_NORMAL = 0
ANGLE_NEGATIVE_Y = 1
ANGLE_NEGATIVE_X = 2
ANGLE_NEGATIVE_XY = 3

# Process name
PROCESS_NAME = ["YuanShen.exe", "GenshinImpact.exe"]

# Screen center points
SCREEN_CENTER_X = 1920/2
SCREEN_CENTER_Y = 1080/2

# stop rules
STOP_RULE_ARRIVE = "ARRIVE"
STOP_RULE_F = 'F_APPEAR'
STOP_RULE_COMBAT = 'COMBAT'

IMG_RATE = 0
IMG_POSI = 1
IMG_POINT = 2
IMG_RECT = 3

LOG_NONE = 0
LOG_WHEN_TRUE = 1
LOG_WHEN_FALSE = 2
LOG_ALL = 3

TEXT_MATCH_CONTAIN_RESULT = 0
TEXT_MATCH_INCLUDED_BY_RESULT = 1
