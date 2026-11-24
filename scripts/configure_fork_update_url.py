#!/usr/bin/env python3
"""Point the inherited app updater at Rev Plays' own GitHub release feed."""
from pathlib import Path

source = Path("core/service/kotlinYtmusicScraper/src/commonMain/kotlin/com/maxrave/kotlinytmusicscraper/Ytmusic.kt")
old = "https://api.github.com/repos/maxrave-dev/SimpMusic/releases/latest"
new = "https://api.github.com/repos/revhuyrr/nxymuisc/releases/latest"
text = source.read_text()
if new in text:
    print("NXYMusic release feed already configured")
elif old in text:
    source.write_text(text.replace(old, new))
    print("Configured the in-app updater to use revhuyrr/nxymuisc releases")
else:
    raise SystemExit("Could not find the expected upstream release URL; refusing to build with an unknown update feed")
