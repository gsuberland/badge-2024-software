# main.py -- put your code here!
from esp32 import Partition

from system.scheduler import scheduler
from system.hexpansion.app import HexpansionManagerApp
from system.patterndisplay.app import PatternDisplay
from system.notification.app import NotificationService
from system.launcher.app import Launcher
from system.power.handler import PowerEventHandler

from frontboards.twentyfour import TwentyTwentyFour


# Start front-board interface
scheduler.start_app(TwentyTwentyFour())

# Start expansion interface
scheduler.start_app(HexpansionManagerApp())

# Start led pattern displayer app
scheduler.start_app(PatternDisplay())

# Start root app
scheduler.start_app(Launcher(), foreground=True)

# Start notification handler
scheduler.start_app(NotificationService(), always_on_top=True)

PowerEventHandler.RegisterDefaultCallbacks(PowerEventHandler)

Partition.mark_app_valid_cancel_rollback()

scheduler.run_forever()
