from src.visualization import (
    plot_top_apps, plot_category, plot_trend,
    plot_weekday, plot_box, plot_productive,
    plot_corr_heatmap, plot_scatter_interactions
)

def analyze_data(df, show=False):
    report = {}
    report['top_apps'] = plot_top_apps(df, show=show)
    report['category'] = plot_category(df, show=show)
    report['trend'] = plot_trend(df, show=show)
    report['weekday'] = plot_weekday(df, show=show)
    report['boxplot'] = plot_box(df, show=show)
    report['productive'] = plot_productive(df, show=show)
    report['corr'] = plot_corr_heatmap(df, show=show)
    report['scatter'] = plot_scatter_interactions(df, show=show)
    return report
