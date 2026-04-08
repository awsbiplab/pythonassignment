
from src.pgds.assignment.dataprocessor.data_loader import load_data
from src.pgds.assignment.dataprocessor.data_cleaning import clean_data
from src.pgds.assignment.dataprocessor.feature_engineering import create_features
from src.pgds.assignment.dataprocessor.merge_data import merge_all

from src.pgds.assignment.analyser.descriptive_analysis import descriptive_analysis
from src.pgds.assignment.analyser.default_analysis import default_risk_analysis
from src.pgds.assignment.analyser.branch_analysis import branch_analysis
from src.pgds.assignment.analyser.customer_analysis import customer_segmentation
from src.pgds.assignment.analyser.statistical_analysis import correlation_analysis
from src.pgds.assignment.analyser.transaction_analysis import transaction_analysis
from src.pgds.assignment.analyser.emi_analysis import emi_analysis
from src.pgds.assignment.analyser.application_analysis import application_analysis
from src.pgds.assignment.analyser.recovery_analysis import recovery_effectiveness
from src.pgds.assignment.analyser.disbursement_analysis import processing_time
from src.pgds.assignment.analyser.profitability_analysis import profitability
from src.pgds.assignment.analyser.geospatial_analysis import geo_analysis
from src.pgds.assignment.analyser.default_trends import default_trends
from src.pgds.assignment.analyser.time_series_analysis import time_series
from src.pgds.assignment.analyser.customer_behavior import customer_behavior
from src.pgds.assignment.analyser.risk_analysis import risk_matrix
from src.pgds.assignment.analyser.time_to_default import time_to_default
from src.pgds.assignment.analyser.transaction_pattern import transaction_pattern

from src.pgds.assignment.visualizer.plots import plot_all
from src.pgds.assignment.reporting.report_generator import generate_full_report
from src.pgds.assignment.analyser.default_analysis import default_risk_analysis
from src.pgds.assignment.visualizer.plots import plot_default_risk
from src.pgds.assignment.analyser.branch_analysis import branch_performance
from src.pgds.assignment.visualizer.plots import plot_branch_performance
from src.pgds.assignment.analyser.customer_analysis import customer_segmentation
from src.pgds.assignment.visualizer.plots import plot_customer_segments

from src.pgds.assignment.analyser.statistical_analysis import advanced_statistical_analysis
from src.pgds.assignment.visualizer.plots import plot_statistical_analysis
from src.pgds.assignment.analyser.transaction_analysis import transaction_and_recovery_analysis
from src.pgds.assignment.visualizer.plots import plot_transaction_recovery

from src.pgds.assignment.analyser.emi_analysis import emi_analysis
from src.pgds.assignment.visualizer.plots import plot_emi_analysis

def main():
    data = load_data()
    data = clean_data(data)
    data = create_features(data)

    df = merge_all(data)

    descriptive_analysis(df)
    default_risk_analysis(df)
    branch_analysis(df)
    customer_segmentation(df)
    correlation_analysis(df)
    profitability(df)

    # DEFAULT RISK
    default_results = default_risk_analysis(df, data['branches'])

    # HEATMAP
    plot_default_risk(df)

#4
    # BRANCH PERFORMANCE
    branch_results = branch_performance(
        df,
        applications=data['applications'],
        defaults=data['defaults']
    )

    # VISUALS
    plot_branch_performance(df)

    # CUSTOMER SEGMENTATION
    customer_results = customer_segmentation(df)

    # VISUALS
    plot_customer_segments(customer_results['df'])

    # ADVANCED STATISTICS
    stats = advanced_statistical_analysis(
        df,
        branches=data['branches'],
        defaults=data['defaults']
    )

    # VISUALS
    plot_statistical_analysis(df, data['defaults'])

    # TRANSACTION & RECOVERY
    trans_results = transaction_and_recovery_analysis(
        df,
        data['transactions'],
        data['defaults'],
        data['branches']
    )

    # VISUALS
    plot_transaction_recovery(
        df,
        data['transactions'],
        data['defaults']
    )
    # EMI ANALYSIS
    emi_results = emi_analysis(df)

    # VISUALS
    plot_emi_analysis(df)
#---
    plot_all(df)
    generate_full_report(df)

    print("ALL TASKS COMPLETED")

if __name__ == "__main__":
    main()
