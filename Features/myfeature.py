"""Basic feature module for the DevAscDemo project."""

from __future__ import annotations


def get_feature_info() -> str:
    """Return a short description of the feature."""
    return "MyFeature is a basic reusable component for DevAscDemo."


def run_feature(name: str) -> str:
    """Run the feature logic and return a result string."""
    print(f"Running feature for {name}...")
    return f"Feature executed for {name}."


__all__ = ["get_feature_info", "run_feature"]
