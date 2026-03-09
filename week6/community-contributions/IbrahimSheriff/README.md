# Support Ticket → Category Classifier

Week 6 community contribution: classify support messages into **Billing**, **Shipping**, **Technical**, **Refund**, or **Other**.

## Dataset

- **support_tickets.csv**: 500 rows, columns `message`, `category`.
- Synthetic support-style messages, roughly 100 per category.
- To regenerate: `python generate_dataset.py` (optional).

## Categories

- Billing, Shipping, Technical, Refund, Other

## How to run

1. Ensure `support_tickets.csv` is in this folder (or run `python generate_dataset.py`).
2. Set `OPENROUTER_API_KEY` in your environment or `.env` (get a key at [openrouter.ai](https://openrouter.ai)).
3. Open `support_ticket_classifier.ipynb` and run all cells.

Dependencies: `pandas`, `scikit-learn`, `openai`, `python-dotenv` (same as course). LLM calls go via OpenRouter (OpenAI-compatible client).

## What the notebook does

- Loads the CSV and splits 80% train / 20% test (stratified).
- **Baseline**: keyword rules + majority-class fallback; reports accuracy and weighted F1.
- **LLM**: OpenRouter (default model `openai/gpt-4o-mini`) with a single prompt (reply with only the category name); same metrics.
- **Comparison**: prints Baseline vs LLM accuracy and F1.

No fine-tuning in this minimal version.
