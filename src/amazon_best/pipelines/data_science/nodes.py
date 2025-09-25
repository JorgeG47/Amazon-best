"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 1.0.0
"""
# src/amazon_best/pipelines/data_science/nodes.py

import pandas as pd
from typing import Dict, Any, Tuple
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import logging

def dividir_datos(data: pd.DataFrame, parameters: Dict[str, Any]) -> Tuple:
    """Divide los datos en conjuntos de entrenamiento y prueba."""
    X = data[parameters["features"]]
    y = data[parameters["target"]]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=parameters["test_size"], random_state=parameters["random_state"], stratify=y
    )
    return X_train, X_test, y_train, y_test

def entrenar_modelo(X_train: pd.DataFrame, y_train: pd.Series) -> RandomForestClassifier:
    """Entrena un modelo de clasificación RandomForest."""
    logging.info("Entrenando el modelo...")
    classifier = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
    classifier.fit(X_train, y_train)
    logging.info("✅ Modelo entrenado exitosamente.")
    return classifier

def evaluar_modelo(model: RandomForestClassifier, X_test: pd.DataFrame, y_test: pd.Series) -> Dict[str, Any]:
    """Evalúa el modelo y devuelve las métricas en un diccionario."""
    logging.info("Evaluando el modelo...")
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True)
    
    logging.info(f"📊 Precisión (Accuracy) del modelo: {accuracy:.4f}")
    
    metrics = {"accuracy": accuracy, "classification_report": report}
    return metrics

def generar_predicciones(model: RandomForestClassifier, X_test: pd.DataFrame, y_test: pd.Series) -> pd.DataFrame:
    """Realiza predicciones y las une a los datos de prueba para una fácil comparación."""
    logging.info("Generando predicciones finales...")
    predictions = model.predict(X_test)
    
    # Crear un DataFrame con los resultados
    results_df = X_test.copy()
    results_df['rango_precio_real'] = y_test
    results_df['rango_precio_predicho'] = predictions
    
    return results_df