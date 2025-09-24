def generate_report(metrics, trained_model):
    import json
    print("📊 Métricas del modelo:")
    print(json.dumps(metrics, indent=2))
    print("✅ Modelo entrenado disponible para exportación o visualización.")