"""Visualization utilities for SaaS analytics project."""

import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path


class Visualizer:
    """Create visualizations for funnel, A/B testing, and retention analysis."""

    OUTPUT_DIR = Path("images")

    def __init__(self) -> None:
        """Ensure output directory exists."""
        self.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    def plot_funnel(self, funnel_df: pd.DataFrame) -> None:
        """Plot overall user funnel as a bar chart.

        Parameters
        ----------
        funnel_df : pd.DataFrame
            Funnel summary with user counts and conversion rates.
        """
        required_columns = {"step", "users", "conversion_rate"}
        self._validate_required_columns(funnel_df, required_columns)

        fig, ax = plt.subplots(figsize=(8, 5))

        # Plot user counts for each funnel step.
        ax.bar(funnel_df["step"], funnel_df["users"])

        ax.set_title("User Funnel")
        ax.set_xlabel("Step")
        ax.set_ylabel("Number of Users")

        # Annotate bars with user counts and overall conversion rate.
        for i, (users, conversion) in enumerate(
            zip(funnel_df["users"], funnel_df["conversion_rate"])
        ):
            ax.text(
                i,
                users + 50,
                f"{users}\n({conversion:.1%})",
                ha="center",
            )

        fig.tight_layout()
        fig.savefig(self.OUTPUT_DIR / "funnel_chart.png", dpi=300, bbox_inches="tight")

        plt.show()
        plt.close(fig)

    def plot_ab_funnel(self, df: pd.DataFrame) -> None:
        """Plot funnel conversion rates for each experiment group.

        Parameters
        ----------
        df : pd.DataFrame
            Grouped funnel data with conversion rates.
        """
        required_columns = {"group", "step", "conversion_rate"}
        self._validate_required_columns(df, required_columns)

        fig, ax = plt.subplots(figsize=(8, 5))

        # Plot conversion rate curves for each experiment group.
        for group in df["group"].unique():
            group_df = df[df["group"] == group]

            ax.plot(
                group_df["step"],
                group_df["conversion_rate"],
                marker="o",
                label=f"Group {group}",
            )

            # Annotate each point with conversion percentage.
            for step, rate in zip(
                group_df["step"], group_df["conversion_rate"]
            ):
                ax.text(step, rate + 0.02, f"{rate:.1%}", ha="center")

        ax.set_title("Funnel Conversion by Experiment Group")
        ax.set_xlabel("Step")
        ax.set_ylabel("Conversion Rate")
        ax.legend()

        fig.tight_layout()
        fig.savefig(self.OUTPUT_DIR / "ab_funnel.png", dpi=300, bbox_inches="tight")

        plt.show()
        plt.close(fig)

    def plot_retention(self, retention_df: pd.DataFrame) -> None:
        """Plot user retention over time.

        Parameters
        ----------
        retention_df : pd.DataFrame
            Retention data with days since first event and retention rate.
        """
        required_columns = {"days_since_first", "retention_rate"}
        self._validate_required_columns(retention_df, required_columns)

        fig, ax = plt.subplots(figsize=(8, 5))

        # Plot retention curve to show how user engagement changes over time.
        ax.plot(
            retention_df["days_since_first"],
            retention_df["retention_rate"],
            marker="o",
        )

        ax.set_title("User Retention Over Time")
        ax.set_xlabel("Days Since First Event")
        ax.set_ylabel("Retention Rate")

        fig.tight_layout()
        fig.savefig(
            self.OUTPUT_DIR / "retention_curve.png",
            dpi=300,
            bbox_inches="tight",
        )

        plt.show()
        plt.close(fig)

    @staticmethod
    def _validate_required_columns(
        df: pd.DataFrame,
        required_columns: set[str],
    ) -> None:
        """Raise an error if required columns are missing."""
        missing_columns = required_columns - set(df.columns)

        if missing_columns:
            missing_text = ", ".join(sorted(missing_columns))
            raise ValueError(f"Missing required columns: {missing_text}")
