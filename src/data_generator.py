"""Generate a synthetic SaaS product event dataset."""

import numpy as np
import pandas as pd


class DataGenerator:
    """Generate realistic SaaS user event data for analytics projects."""

    DEVICES = ["desktop", "mobile"]
    DEVICE_PROBABILITIES = [0.55, 0.45]

    COUNTRIES = ["US", "CA", "UK", "AU"]
    COUNTRY_PROBABILITIES = [0.55, 0.15, 0.20, 0.10]

    ACQUISITION_CHANNELS = [
        "organic",
        "paid_search",
        "referral",
        "linkedin",
        "email",
    ]
    ACQUISITION_PROBABILITIES = [0.30, 0.25, 0.15, 0.10, 0.20]

    PLAN_TYPES = ["free", "basic", "pro"]
    PLAN_PROBABILITIES = [0.65, 0.25, 0.10]

    def __init__(self, random_seed: int = 42) -> None:
        """Initialize the generator with a fixed random seed."""
        self.random_seed = random_seed
        np.random.seed(self.random_seed)

    def generate_saas_data(self, n_users: int = 2000) -> pd.DataFrame:
        """Generate a synthetic SaaS event dataset.

        Parameters
        ----------
        n_users : int, optional
            Number of users to simulate, by default 2000.

        Returns
        -------
        pd.DataFrame
            Event-level SaaS dataset.
        """
        users = np.arange(1, n_users + 1)
        events = []

        for user_id in users:
            # Assign a realistic first-touch time within the simulation window.
            signup_window_start = pd.Timestamp("2024-01-01")
            first_touch_time = signup_window_start + pd.Timedelta(
                days=np.random.randint(0, 60),
                hours=np.random.randint(0, 24),
            )

            # Assign user-level attributes that remain fixed across events.
            experiment_group = np.random.choice(["A", "B"])
            device = np.random.choice(
                self.DEVICES,
                p=self.DEVICE_PROBABILITIES,
            )
            country = np.random.choice(
                self.COUNTRIES,
                p=self.COUNTRY_PROBABILITIES,
            )
            acquisition_channel = np.random.choice(
                self.ACQUISITION_CHANNELS,
                p=self.ACQUISITION_PROBABILITIES,
            )
            plan_type = np.random.choice(
                self.PLAN_TYPES,
                p=self.PLAN_PROBABILITIES,
            )

            # Simulate a modest treatment effect for experiment group B.
            signup_probability = 0.72 if experiment_group == "B" else 0.68
            activate_probability = 0.58 if experiment_group == "B" else 0.50
            subscribe_probability = 0.36 if experiment_group == "B" else 0.28

            funnel_steps = [
                ("visit", 1.00),
                ("signup", signup_probability),
                ("activate", activate_probability),
                ("subscribe", subscribe_probability),
            ]

            current_time = first_touch_time
            activated_user = False

            # Simulate progression through the SaaS funnel.
            for event_type, probability in funnel_steps:
                if np.random.rand() < probability:
                    events.append(
                        {
                            "user_id": user_id,
                            "event_time": current_time,
                            "event_type": event_type,
                            "plan_type": plan_type,
                            "country": country,
                            "device": device,
                            "acquisition_channel": acquisition_channel,
                            "experiment_group": experiment_group,
                        }
                    )

                    if event_type == "activate":
                        activated_user = True

                    current_time += pd.Timedelta(hours=np.random.randint(2, 72))
                else:
                    break

            # Simulate ongoing usage for users who reached activation.
            if activated_user:
                n_sessions = np.random.randint(1, 8)
                session_time = current_time

                for _ in range(n_sessions):
                    session_time += pd.Timedelta(days=np.random.randint(1, 15))
                    events.append(
                        {
                            "user_id": user_id,
                            "event_time": session_time,
                            "event_type": "session",
                            "plan_type": plan_type,
                            "country": country,
                            "device": device,
                            "acquisition_channel": acquisition_channel,
                            "experiment_group": experiment_group,
                        }
                    )

        df = (
            pd.DataFrame(events)
            .sort_values(["user_id", "event_time"])
            .reset_index(drop=True)
        )

        return df
