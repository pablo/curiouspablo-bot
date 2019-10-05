TOKEN="INSERT-YOUR-TOKEN-HERE-OR-BETTER-IN-LOCAL_SETTINGS.PY"

try:
    from local_settings import TOKEN
except ImportError:
    pass
