

# 🚀 LangChain Basic LLM Chain (Local con Ollama)

## 📖 Descripción General

Este proyecto implementa una **LLM Chain básica utilizando LangChain v1 y un modelo de lenguaje ejecutado localmente con Ollama**.

El objetivo es comprender:

* Cómo se estructuran los prompts en LangChain.
* Cómo se conecta un LLM a una cadena.
* Cómo fluye la información desde el usuario hasta la respuesta generada.
* Cómo ejecutar modelos de lenguaje de manera local sin depender de APIs externas.

A diferencia de implementaciones basadas en OpenAI o Gemini, este proyecto funciona completamente **offline**, utilizando un modelo descargado localmente mediante Ollama.

---

# 🧠 Arquitectura del Sistema

## 🔹 Flujo de ejecución

```
Usuario
   ↓
PromptTemplate
   ↓
LLM (ChatOllama)
   ↓
Respuesta generada
```

## 🔹 Componentes

| Componente            | Rol                                        |
| --------------------- | ------------------------------------------ |
| LangChain Core        | Orquesta la cadena y los prompts           |
| PromptTemplate        | Define la estructura del mensaje al modelo |
| ChatOllama            | Interfaz con el modelo local               |
| Ollama                | Motor que ejecuta el modelo                |
| Modelo (gemma:2b) | Generación de texto                        |

---

# 🏗 Diseño Técnico

Este proyecto utiliza la sintaxis moderna de **LangChain Expression Language (LCEL)**:

```python
chain = prompt | llm
```

Esta arquitectura permite:

* Composición modular
* Encadenamiento declarativo
* Mejor escalabilidad
* Integración futura con RAG o agentes

---

# 💡 ¿Qué hace el programa?

1. Inicializa un modelo local ( `gemma:2b`)
2. Define una plantilla de prompt con una variable `{topic}`
3. Construye una cadena conectando prompt + modelo
4. Solicita un tema al usuario
5. Genera una explicación sencilla sobre el tema

Ejemplo:

```
Enter a topic: Neural Networks
```

Salida:

```
Neural networks are computer systems inspired by how the human brain works...
```

---

# ⚙️ Requisitos

* Python 3.10+
* Ollama instalado
* Modelo descargado
* pip

---

# 🚀 Instalación Paso a Paso

## 1️⃣ Instalar Ollama

Linux / Mac:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Verificar:

```bash
ollama --version
```

---

## 2️⃣ Descargar un modelo

Ejemplo con Gemma:

```bash
ollama pull gemma:2b
```

Otros modelos compatibles:

* `llama3`
* `mistral`
* `phi3`

---

## 3️⃣ Instalar dependencias

Dentro del proyecto:

```bash
pip install -r requirements.txt
```

O manualmente:

```bash
pip install langchain langchain-community
```

---

## 4️⃣ Ejecutar

```bash
python main.py
```

---

# 📂 Estructura del Proyecto

```
LangChain-Basic-LLM-Chain/
│
├── main.py
├── README.md
└── requirements.txt
```

---

# 🎯 ¿Por qué usar Ollama en este proyecto?

| OpenAI API        | Ollama                 |
| ----------------- | ---------------------- |
| Requiere API key  | ❌ No requiere API key  |
| Tiene costo       | ❌ Gratis               |
| Requiere internet | ❌ Funciona offline     |
| Depende de cuotas | ❌ Sin límites externos |

Ideal para:

* Desarrollo local
* Laboratorios académicos
* Prototipado rápido
* Pruebas sin costos

---

# 🔍 Posibles Extensiones Futuras

Este proyecto puede evolucionar hacia:

* 🔎 Implementación de RAG (Retrieval-Augmented Generation)
* 🤖 Agentes con herramientas
* 📚 Indexación de documentos
* 🧠 Sistemas multi-agente
* 🌐 API REST con FastAPI

---

# 📘 Aprendizajes Clave

* Cómo funciona una LLM Chain en LangChain
* Diferencia entre APIs externas y modelos locales
* Arquitectura básica de sistemas LLM
* Modularidad usando LCEL
* Integración futura con arquitecturas RAG

---

# 🧾 Conclusión

Este repositorio demuestra la implementación mínima funcional de una cadena LLM utilizando un modelo local con Ollama.

Proporciona una base sólida para construir sistemas más complejos como RAGs o agentes inteligentes.

---

