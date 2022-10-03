# Convert Cordinape to Quadratic Funding

## How to use

Copy cordinape results to `files/data.json`

```graphql
query PerPersonGive {
  token_gifts(where: { epoch_id: { _eq: 8576 } }) {
    sender_id
    sender_address
    recipient_id
    recipient_address
    tokens
  }
}
```

output will be generated at `files/output.csv`
