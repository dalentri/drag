DRAG, a Document Search API

A lightweight, cost-effective Retrieval-Augmented Generation (RAG) API built for efficient document search and context-aware LLM responses.

## Tech Stack

- **Framework:** FastAPI
- **Orchestration:** LlamaIndex
- **Database:** PostgreSQL with `pgvector` extension
- **Dependency Management:** `uv`
- **Hosting:** Render

## Architecture

![Architecture Diagram](./Media/diagram.png)

## Local Development & Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Install dependencies using `uv`:**

   ```bash
   uv sync
   ```

3. **Configure environment variables:**
   Create a `.env` file in the root directory and add your credentials:

   ```env
   OPEN_API_KEY=your_open_api_key_here
   DATABASE_URL=postgresql://user:password@localhost:5432/dbname
   MODEL=model_name
   ```

4. **Run the development server:**

   ```bash
   uv run
   ```
