"""Backward-compatible alias for :class:`Supervisor`."""

from .agents import Supervisor


class GeoAIAgent(Supervisor):
    """Alias for :class:`Supervisor` providing legacy name."""

    pass
