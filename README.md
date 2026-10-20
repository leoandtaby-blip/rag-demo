# RAG Demo

A small Python project that shows the retrieval step of RAG (retrieval-augmented generation). Given a question, it searches a set of text files and returns the most relevant one.

## How it works

1. `load_documents()` reads every `.txt` file in the folder.
2. `get_words()` turns text into a set of lowercase words.
3. `find_best_match()` scores each file by how many words it shares with the question and returns the best match.

## Example

Question: "How much does express delivery cost?"
Best matching file: `shipping.txt`

## Run it

```
python retrieve.py
```

## Limitations

- Matching is based on exact shared words, so it can miss files that use different wording for the same idea.

## Next steps

- Replace keyword matching with embeddings for meaning-based search.
- Send the matched text and the question to Claude to generate the final answer.