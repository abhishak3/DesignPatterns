from __future__ import annotations
from threading import Lock


class Singleton:
    """
    Thread-safe Singleton implementation.
    Ensures only one instance exists.
    """

    _instance: Singleton | None = None
    _lock: Lock = Lock()

    def __new__(cls) -> Singleton:
        # Double-checked locking for thread safety
        if cls._instance is None: # not allowing every caller to acquire lock - performance check
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        # __init__ may run multiple times in Python singletons.
        # Guard against reinitialization.
        if getattr(self, "_initialized", False):
            return

        self._initialized = True
        self.config: dict[str, str] = {}

    def set(self, key: str, value: str) -> None:
        self.config[key] = value

    def get(self, key: str) -> str | None:
        return self.config.get(key)
