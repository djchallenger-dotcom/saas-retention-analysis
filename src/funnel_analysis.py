"""Funnel analysis utilities for SaaS user conversion."""

import pandas as pd


class FunnelAnalyzer:
    """Analyze user progression through a SaaS conversion funnel."""

    FUNNEL_STEPS = ["visit", "signup", "activate", "subscribe"]

    def build_funnel(self, df: pd.DataFrame) -> pd.DataFrame:
        """Compute user counts and conversion metrics for each funnel stage.

        Parameters
        ----------
        df : pd.DataFrame
            Event-level SaaS dataset containing at least `user_id` and
            `event_type` columns.

        Returns
        -------
        pd.DataFrame
            Funnel summary with user counts, overall conversion rates, and
            step-to-step conversion rates.
        """
        required_columns = {"user_id", "event_type"}
        self._validate_required_columns(df, required_columns)

        funnel_rows = []

        # Count how many unique users reached each step of the funnel.
        for step in self.FUNNEL_STEPS:
            user_count = df[df["event_type"] == step]["user_id"].nunique()
            funnel_rows.append({"step": step, "users": user_count})

        funnel_df = pd.DataFrame(funnel_rows)

        # Overall conversion is measured relative to the first funnel step.
        funnel_df["conversion_rate"] = (
            funnel_df["users"] / funnel_df["users"].iloc[0]
        )

        # Step conversion measures retention from the immediately previous step.
        funnel_df["step_conversion"] = (
            funnel_df["users"] / funnel_df["users"].shift(1)
        )

        return funnel_df

    def print_funnel_summary(self, funnel_df: pd.DataFrame) -> None:
        """Print a readable text summary of funnel performance.

        Parameters
        ----------
        funnel_df : pd.DataFrame
            Funnel summary returned by `build_funnel`.
        """
        required_columns = {"step", "users", "conversion_rate", "step_conversion"}
        self._validate_required_columns(funnel_df, required_columns)

        print("\nFunnel Summary:\n")

        for index, row in funnel_df.iterrows():
            step = row["step"]
            users = row["users"]
            conversion_rate = row["conversion_rate"]

            if index == 0:
                print(f"{step}: {users} users")
            else:
                step_conversion = row["step_conversion"]
                print(
                    f"{step}: {users} users "
                    f"({step_conversion:.2%} from previous step, "
                    f"{conversion_rate:.2%} overall)"
                )

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
