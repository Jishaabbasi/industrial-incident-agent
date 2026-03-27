# Industrial Incident Summarizer Agent

AI agent built using ADK and Gemini for summarizing industrial incident reports.

## Features
- ADK Agent
- Gemini inference
- FastAPI endpoint
- Cloud Run deployment

## Endpoint
POST /summarize

## Sample Input
{
"text":"Operator observed overheating in conveyor motor."
}

## Sample Output
{
"summary":"Conveyor motor overheating detected."
}