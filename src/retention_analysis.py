"""Retention analysis for SaaS users."""

import pandas as pd


class RetentionAnalyzer:
    """Analyze user retention based on session activity over time."""

    def compute_retention(self, df: pd.DataFrame) -> pd.DataFrame:
        """Compute retention rates by days since first user activity.

        Parameters
        ----------
        df : pd.DataFrame
            Event-level SaaS dataset containing `user_id`, `event_time`,
            and `event_type`.

        Returns
        -------
        pd.DataFrame
            DataFrame with:
            - days_since_first
            - user_id (unique users active that day)
            - retention_rate (relative to total users)
        """
        required_columns = {"user_id", "event_time", "event_type"}
        self._validate_required_columns(df, required_columns)

        df = df.copy()

        # Identify the first activity timestamp for each user.
        # This serves as the baseline for measuring retention.
        first_event_df = (
            df.groupby("user_id")["event_time"]
            .min()
            .reset_index()
            .rename(columns={"event_time": "first_event_time"})
        )

        # Merge first event time back onto the main dataset.
        df = df.merge(first_event_df, on="user_id")

        # Calculate the number of days since each user's first interaction.
        df["days_since_first"] = (
            df["event_time"] - df["first_event_time"]
        ).dt.days

        # Retention is typically measured based on returning activity,
        # so we focus on session events.
        session_df = df[df["event_type"] == "session"]

        # Count how many unique users are active on each day since first event.
        retention_df = (
            session_df.groupby("days_since_first")["user_id"]
            .nunique()
            .reset_index()
        )

        # Normalize by total number of users to compute retention rate.
        total_users = df["user_id"].nunique()
        retention_df["retention_rate"] = (
            retention_df["user_id"] / total_users
        )

        return retention_df

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
