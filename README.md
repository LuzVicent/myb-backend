#  Mind Your Business (MYB) - Analizador de Nóminas con IA

**MYB** es una aplicación Full Stack diseñada para empoderar a los trabajadores, ayudándoles a entender sus nóminas mediante Inteligencia Artificial, garantizando siempre la privacidad de sus datos.

## 🛠 Backend Stack

![Python](https://img.shields.io/badge/Python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688.svg?style=for-the-badge&logo=fastapi&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=openai&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248.svg?style=for-the-badge&logo=mongodb&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED.svg?style=for-the-badge&logo=docker&logoColor=white)

---

## 🚀 Core Features

### 📄 Intelligent OCR
- Extracción de texto desde **PDFs e imágenes**
- Uso combinado de `PyMuPDF` y `EasyOCR`

### 🔐 Privacy by Design
- Sistema propio de **anonimización**
- Detección y censura automática de:
  - Nombres y apellidos
  - DNI / NIE
  - IBAN y cuentas bancarias
- **Ningún dato sensible** se envía a servicios externos

### 🤖 AI-Powered Analysis
- Integración con **OpenAI (GPT-4o)**
- Explicación clara de:
  - Conceptos legales de la nómina
  - Complementos salariales
  - Deducciones y retenciones
- Verificación de cálculos salariales básicos

### 🧱 Clean Architecture
- Separación clara de responsabilidades:
  - Controllers (API)
  - Services (lógica de negocio)
  - Utils (OCR, anonimización, parsing)
- Código preparado para **escalar y mantenerse**

---
