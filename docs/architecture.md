# AtlasIQ - AI Financial Research Assistant

## Version

v1.0 (MVP)

---

# Vision

AtlasIQ is an AI-powered Financial Research Assistant designed to help financial analysts, investors, and students analyze company annual reports using Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG).

The objective is to reduce the time required to understand financial documents while providing trustworthy, source-backed answers.

---

# Problem Statement

Annual reports are often 200–500 pages long.

Finding specific financial information such as:

- Revenue
- Net Profit
- Debt
- Risks
- Cash Flow
- Management Discussion

requires significant manual effort.

Existing chatbots provide generic answers and frequently hallucinate because they are not grounded in the uploaded financial document.

AtlasIQ solves this problem using Retrieval-Augmented Generation (RAG), enabling accurate, document-aware responses with citations.

---

# Target Users

### Primary Users

- Financial Analysts
- Investment Analysts
- Equity Research Analysts
- MBA Finance Students

### Secondary Users

- Retail Investors
- Chartered Accountants
- Finance Researchers

---

# Objectives

- Analyze company annual reports
- Provide source-backed answers
- Reduce research time
- Improve financial understanding
- Build a production-grade AI assistant

---

# MVP Features

## Document Upload

Users can upload company annual reports in PDF format.

---

## Intelligent Search

The system retrieves only relevant sections from the uploaded report.

---

## Financial Question Answering

Example questions:

- What is the company's revenue?
- What are the major risks?
- Summarize the annual report.
- Explain the management discussion.
- What changed compared to last year?

---

## Source Citation

Every response should contain page references.

Example:

Revenue increased by 14%.

Source:
Annual Report
Page 82

---

## Financial Dashboard

Automatically extract and display:

- Revenue
- Net Profit
- Assets
- Liabilities
- Cash Flow

---

# Technology Stack

Frontend

- Streamlit

Backend

- FastAPI

Programming Language

- Python

LLM

- OpenAI GPT

Framework

- LangChain

Agent Framework

- LangGraph

Vector Database

- ChromaDB

Database

- SQLite (MVP)

Deployment

- Docker

Version Control

- Git + GitHub

---

# High-Level Architecture

User

↓

Streamlit UI

↓

FastAPI

↓

RAG Pipeline

↓

ChromaDB

↓

OpenAI

↓

Response + Citations

---

# Project Structure

atlas-ai/

app/
Main application entry point

backend/
FastAPI APIs

frontend/
Streamlit interface

rag/
Document processing and retrieval pipeline

agents/
AI agents

data/
Sample annual reports

docs/
Project documentation

tests/
Testing

---

# Future Roadmap

Version 2

- Multi-company comparison
- Earnings call analysis
- Financial ratio calculations
- Interactive dashboards

Version 3

- Multi-agent architecture
- Portfolio analysis
- News intelligence
- Stock analysis

Version 4

- Cognitive Finance Platform
- AI Investment Copilot
- Portfolio Recommendation Engine

---

# Success Metrics

The MVP will be considered successful if it can:

- Upload an annual report
- Answer financial questions accurately
- Provide citations
- Return responses in under 5 seconds