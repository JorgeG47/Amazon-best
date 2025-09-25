"""
This is a boilerplate pipeline 'data_engeenering'
generated using Kedro 1.0.0
"""
# src/amazon_best/pipelines/data_engineering/nodes.py

import pandas as pd
import re
from typing import Dict, Any

def _limpiar_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Función auxiliar para aplicar la limpieza básica."""
    df.drop_duplicates(inplace=True)
    df.fillna(0, inplace=True)
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].astype(str).apply(lambda x: re.sub(r'[^\w\s\.\-]', '', x))
    return df

def unir_y_crear_caracteristicas(
    amazon: pd.DataFrame,
    products: pd.DataFrame,
    categories: pd.DataFrame,
    extra_products: pd.DataFrame,
    params: Dict[str, Any]
) -> pd.DataFrame:
    """
    Une todos los dataframes y crea las características finales, incluida la variable objetivo.
    """
    # 1. Limpiar todos los dataframes de entrada
    amazon_clean = _limpiar_dataframe(amazon)
    products_clean = _limpiar_dataframe(products)
    categories_clean = _limpiar_dataframe(categories)
    extra_products_clean = _limpiar_dataframe(extra_products)

    # 2. Renombrar columnas para facilitar las uniones
    products_clean = products_clean.rename(columns={'title': 'product_name'})
    categories_clean = categories_clean.rename(columns={'id': 'category_id'})

    # 3. Realizar las uniones (merge)
    df_merged = pd.merge(amazon_clean, extra_products_clean, on='product_id', how='left')
    df_merged = pd.merge(df_merged, categories_clean, on='category_id', how='left')
    
    # 4. Ingeniería de Características (Feature Engineering)
    print("🛠️  Creando nuevas características...")
    
    # Asegurar que las columnas sean numéricas, manejando errores
    for col in ['price', 'discounted_price', 'rating_count', 'discount_percentage']:
        df_merged[col] = pd.to_numeric(df_merged[col], errors='coerce').fillna(0)
    df_merged['rating'] = pd.to_numeric(df_merged['rating_x'], errors='coerce').fillna(0)
    
    # Crear la variable objetivo: 'rango_precio' usando los parámetros
    df_merged['rango_precio'] = pd.cut(
        df_merged['discounted_price'],
        bins=params["price_range_bins"],
        labels=params["price_range_labels"],
        include_lowest=True
    )
    
    # Eliminar filas donde el objetivo es nulo
    df_merged.dropna(subset=['rango_precio'], inplace=True)
    
    print(f"✅ Preprocesamiento completo. Forma final del dataset: {df_merged.shape}")
    
    return df_merged