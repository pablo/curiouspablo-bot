TOKEN="INSERT-YOUR-TOKEN-HERE-OR-BETTER-IN-LOCAL_SETTINGS.PY"
IEXAPIS_API_KEY="INSERT-YOUR-API-KEY-HERE-OR-BETTER-IN-LOCAL_SETTINGS.PY"
COINMARKETCAP_API_KEY="INSERT-YOUR-COINMARKETCAP-API-KEY-HERE-OR-BETTER-IN-LOCAL_SETTINGS.PY"

GABBIE_DIR="/tmp/pics"

try:
    from local_settings import *
except ImportError:
    pass
