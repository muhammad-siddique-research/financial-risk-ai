"""
Financial Risk Prediction Pipeline

Author:
Muhammad Siddique

Purpose:
End-to-end reproducible training pipeline for corporate
bankruptcy risk prediction using econometric and machine
learning approaches.
"""


import joblib
import pandas as pd


from src.config import (
    DATA_PATH,
    MODEL_DIR
)


from src.preprocessing import (
    load_data,
    separate_features_target,
    split_data,
    scale_features
)


from src.feature_engineering import (
    prepare_features
)


from src.models import (
    get_all_models
)


from src.evaluation import (
    evaluate_model
)


from src.utils import (
    save_message
)



def main():

    save_message(
        "Starting Financial Risk Prediction Pipeline"
    )


    # -----------------------------
    # Load dataset
    # -----------------------------

    df = load_data(
        DATA_PATH
    )


    print(
        "Dataset loaded:",
        df.shape
    )


    # -----------------------------
    # Feature-target separation
    # -----------------------------

    X, y = separate_features_target(
        df
    )


    # -----------------------------
    # Feature engineering
    # -----------------------------

    X = prepare_features(
        X
    )


    # -----------------------------
    # Train-test split
    # -----------------------------

    X_train, X_test, y_train, y_test = split_data(
        X,
        y
    )


    # -----------------------------
    # Scaling
    # -----------------------------

    X_train_scaled, X_test_scaled, scaler = scale_features(
        X_train,
        X_test
    )


    joblib.dump(
        scaler,
        f"{MODEL_DIR}/scaler.pkl"
    )


    # -----------------------------
    # Model training
    # -----------------------------

    models = get_all_models()


    results = []


    for name, model in models.items():


        print(
            f"Training {name}"
        )


        model.fit(
            X_train_scaled,
            y_train
        )


        # Save model

        filename = (
            name.lower()
            .replace(" ", "_")
        )


        joblib.dump(
            model,
            f"{MODEL_DIR}/{filename}.pkl"
        )


        # Evaluation

        metrics = evaluate_model(
            model,
            X_test_scaled,
            y_test
        )


        metrics["Model"] = name


        results.append(
            metrics
        )


    # -----------------------------
    # Save results
    # -----------------------------

    results_df = pd.DataFrame(
        results
    )


    results_df.to_csv(
        "results/model_results.csv",
        index=False
    )


    save_message(
        "Training completed successfully"
    )


    print(results_df)



if __name__ == "__main__":

    main()
