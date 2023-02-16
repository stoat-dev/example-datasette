# example-datasette

```
docker run --name example-datasette-db -p 5432:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres -d postgres
```

```
python3 -m venv env
pip install -r requirements.txt
source env/bin/activate
export DATABASE_URL=postgresql://postgres:postgres@localhost:5432/postgres
python -m pytest
```
