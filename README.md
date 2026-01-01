# Mind Your Business (MYB) - Analizador de Nóminas con IA 🧠💰

**MYB** es una aplicación **LegalTech** Full Stack diseñada para empoderar a los trabajadores. Ayuda a entender nóminas complejas, detectar errores y visualizar la evolución salarial mediante Inteligencia Artificial, garantizando siempre la privacidad del usuario.

## 🛠 Backend Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)

---

## 🚀 Core Features

### 💾 Persistencia & CRUD (MongoDB)
- Implementación de base de datos NoSQL con **MongoDB** (Dockerized).
- Uso de **Beanie ODM** (Asynchronous Object-Document Mapper) para una gestión de datos eficiente y tipada.
- Historial completo: **Create** (Subir), **Read** (Historial/Detalle), **Delete** (Gestión de errores).

### 📄 Intelligent OCR & Vision
- Sistema híbrido de extracción de datos:
  - **PDFs:** Procesamiento nativo con `PyMuPDF` y limpieza con Regex.
  - **Imágenes:** Análisis visual avanzado con **GPT-4o Vision** para nóminas escaneadas o fotografías.
  - **Fallback:** Integración con `EasyOCR` local para pre-procesado.

### 🔐 Privacy by Design (GDPR Friendly)
- Sistema propio de **anonimización en capas**:
  - **Capa 1 (Regex):** Eliminación de patrones fijos (DNI, NIE, IBAN, Teléfonos).
  - **Capa 2 (NLP - SpaCy):** Reconocimiento de Entidades Nombradas (NER) para detectar y censurar nombres de personas y ubicaciones.
- **Zero-Knowledge:** A la IA solo llega el texto censurado.

### 🤖 AI-Powered Analysis
- Integración con la API de **OpenAI**.
- Transformación de datos no estructurados a **JSON estructurado**.
- Explicación de conceptos legales y generación de consejos financieros personalizados.

### 📡 Observabilidad & Logs
- Sistema de **Logging Centralizado** (`logging` module).
- Trazabilidad completa de errores y eventos operativos.
- Generación de archivos de log persistentes (`myb_app.log`) para depuración y mantenimiento en producción.

---

## 🏗️ Arquitectura del Proyecto

El proyecto sigue una arquitectura modular y escalable, separando claramente las responsabilidades:

```text
/backend
├── /api          # Endpoints (Routers) definidos por dominio (Upload, Analyze, History)
├── /services     # Lógica de negocio pura (OpenAI, OCR, Anonimizador)
├── /orm          # Capa de datos (Modelos de BD, conexión Mongo)
├── /tmp          # Gestión de archivos temporales (limpieza automática)
└── main.py       # Punto de entrada y configuración de Logs/CORS
