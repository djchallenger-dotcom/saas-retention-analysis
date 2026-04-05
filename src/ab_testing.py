"""A/B testing analysis for SaaS funnel performance."""

import pandas as pd


class ABTester:
    """Analyze funnel performance across experiment groups."""

    FUNNEL_STEPS = ["visit", "signup", "activate", "subscribe"]

    def build_group_funnel(self, df: pd.DataFrame) -> pd.DataFrame:
        """Compute funnel user counts for each experiment group.

        Parameters
        ----------
        df : pd.DataFrame
            Event-level SaaS dataset containing `user_id`, `event_type`,
            and `experiment_group`.

        Returns
        -------
        pd.DataFrame
            DataFrame containing user counts for each funnel step
            per experiment group.
        """
        required_columns = {"user_id", "event_type", "experiment_group"}
        self._validate_required_columns(df, required_columns)

        results = []

        # Iterate through each experiment group (e.g., A and B)
        # and compute how many users reach each step of the funnel.
        for group in df["experiment_group"].unique():
            group_df = df[df["experiment_group"] == group]

            for step in self.FUNNEL_STEPS:
                user_count = group_df[
                    group_df["event_type"] == step
                ]["user_id"].nunique()

                results.append(
                    {
                        "group": group,
                        "step": step,
                        "users": user_count,
                    }
                )

        return pd.DataFrame(results)

    def add_conversion_rates(self, df: pd.DataFrame) -> pd.DataFrame:
        """Add conversion metrics to a grouped funnel DataFrame.

        Parameters
        ----------
        df : pd.DataFrame
            Output of `build_group_funnel`.

        Returns
        -------
        pd.DataFrame
            DataFrame with additional columns:
            - conversion_rate (relative to first step)
            - step_conversion (relative to previous step)
        """
        required_columns = {"group", "step", "users"}
        self._validate_required_columns(df, required_columns)

        df = df.copy()

        # Compute overall conversion relative to the first funnel step
        # within each experiment group.
        df["conversion_rate"] = df.groupby("group")["users"].transform(
            lambda x: x / x.iloc[0]
        )

        # Compute step-to-step conversion within each group.
        df["step_conversion"] = df.groupby("group")["users"].transform(
            lambda x: x / x.shift(1)
        )

        return df

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
