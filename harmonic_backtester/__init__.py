from .signals import collect_signals
from .evaluation import evaluate_signal, evaluate_all
from .metrics import compute_statistics
from .visualize import plot_returns, plot_patterns

__all__ = [
    "collect_signals",
    "evaluate_signal",
    "evaluate_all",
    "compute_statistics",
    "plot_returns",
    "plot_patterns",
]