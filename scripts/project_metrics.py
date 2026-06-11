import pandas as pd

metrics = {
    "Metric":[
        "Raw Variants",
        "Filtered Variants",
        "SNPs",
        "INDELs",
        "Missense",
        "Frameshift",
        "Stop Gained"
    ],
    "Count":[
        75717,
        3488,
        3315,
        173,
        1028,
        21,
        11
    ]
}

df = pd.DataFrame(metrics)

df.to_csv(
    "results/project_metrics.csv",
    index=False
)

print(df)
