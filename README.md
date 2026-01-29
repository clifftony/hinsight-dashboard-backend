# hinsight-dashboard-backend (FastAPI)
Building a secure, auditable platform that aggregates health-related data from multiple sources, normalizes it into consistent measures for the 8 well-being factors (sleep, nutrition, stress, depression, smoking, obesity, wellness, movement), and serves decision-support dashboards and insights for authorized users
## Local setup
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

pip install -e ".[dev]"
uvicorn app.main:app --reload