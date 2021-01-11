TOKEN="INSERT-YOUR-TOKEN-HERE-OR-BETTER-IN-LOCAL_SETTINGS.PY"
IEXAPIS_API_KEY="INSERT-YOUR-API-KEY-HERE-OR-BETTER-IN-LOCAL_SETTINS.PY"

try:
    from local_settings import TOKEN
except ImportError:
    pass

try:
    from local_settings import IEXAPIS_API_KEY
except ImportError:
    pass


