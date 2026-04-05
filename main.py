"""
Run the SaaS retention and funnel analysis pipeline.

This script generates a synthetic SaaS event dataset, analyzes user funnel
performance, compares experiment groups, computes retention behavior, and
produces visualizations used in the project report.
"""

from src.ab_testing import ABTester
from src.data_generator import DataGenerator
from src.funnel_analysis import FunnelAnalyzer
from src.retention_analysis import RetentionAnalyzer
from src.visualizer import Visualizer


# Configuration values used by the main workflow.
N_USERS = 2000
PREVIEW_ROWS = 10


def main() -> None:
    """Execute the full SaaS analytics workflow."""
    # Create helper objects for each stage of the analysis pipeline.
    generator = DataGenerator()
    funnel_analyzer = FunnelAnalyzer()
    ab_tester = ABTester()
    retention_analyzer = RetentionAnalyzer()
    visualizer = Visualizer()

    # Generate a synthetic event-level SaaS dataset.
    # This dataset is the foundation for all downstream analyses.
    df = generator.generate_saas_data(n_users=N_USERS)

    # Display a quick preview so the user can inspect the structure and
    # confirm that the synthetic events were generated as expected.
    print("Dataset Preview:")
    print(df.head(PREVIEW_ROWS))

    print("\nDataset Shape:")
    print(df.shape)

    print("\nEvent Counts:")
    print(df["event_type"].value_counts())

    # Build the overall funnel to measure user progression from visit
    # through subscription and identify major drop-off points.
    funnel_df = funnel_analyzer.build_funnel(df)

    print("\nFunnel Data:")
    print(funnel_df)

    funnel_analyzer.print_funnel_summary(funnel_df)

    # Visualize the overall funnel so conversion performance is easy to
    # interpret and include in the project README.
    visualizer.plot_funnel(funnel_df)

    # Build experiment-group funnel data to compare groups A and B.
    # This helps measure the impact of the simulated product change.
    group_funnel_df = ab_tester.build_group_funnel(df)
    group_funnel_df = ab_tester.add_conversion_rates(group_funnel_df)

    print("\nA/B Funnel Data:")
    print(group_funnel_df)

    # Plot experiment-group conversion performance across the funnel.
    visualizer.plot_ab_funnel(group_funnel_df)

    # Compute retention behavior using session activity over time.
    # This shows how user engagement changes after first interaction.
    retention_df = retention_analyzer.compute_retention(df)

    print("\nRetention Data:")
    print(retention_df.head(PREVIEW_ROWS))

    # Plot the retention curve to visualize how user return rates decline
    # over time, which is a key SaaS product metric.
    visualizer.plot_retention(retention_df)

    print("\nSaaS analytics pipeline completed successfully.")


if __name__ == "__main__":
    main()
