# Calculator Python

[![CI con SonarQube](https://github.com/LeandroTombe/testsonar/actions/workflows/ci.yml/badge.svg)](https://github.com/LeandroTombe/testsonar/actions/workflows/ci.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=LeandroTombe_testsonar&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=LeandroTombe_testsonar)

Calculadora simple en Python con análisis de calidad de código mediante SonarQube Cloud.

## Configuración de SonarQube

Para que el CI funcione correctamente, necesitas:

1. **Agregar el token de SonarQube como secreto en GitHub:**
   - Ve a tu repositorio en GitHub
   - Settings → Secrets and variables → Actions
   - Click en "New repository secret"
   - Nombre: `SONAR_TOKEN`
   - Valor: Tu token de SonarQube Cloud (puedes generarlo en https://sonarcloud.io/account/security/)

2. **El proyecto ya está configurado con:**
   - Organization: `leandrotombe`
   - Project Key: `LeandroTombe_testsonar`

## Uso

```bash
python main.py
```

## Operaciones disponibles

- `add` - Suma
- `subtract` - Resta
- `multiply` - Multiplicación
- `divide` - División
- `sqrt` - Raíz cuadrada
- `exit` - Salir

## CI/CD

El workflow de GitHub Actions se ejecuta automáticamente en cada push o pull request y:
- ✅ Analiza el código con SonarQube Cloud
- ✅ Verifica el Quality Gate
- ✅ Reporta problemas de calidad y seguridad
