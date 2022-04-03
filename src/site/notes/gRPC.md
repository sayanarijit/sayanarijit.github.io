---
layout: note
tags:
  - tech
  - computer-science
---

# gRPC

gRPC is a type-safe client-server communication framework (not necessarily for the web) with a big focus on performance. It can generate code from a schema definition like GraphQL[^1] does.

## Tips

- Should be idempotent
- Should have timeout
- field 0 = default/unknown
- Don't include error messages in response
- Don't batch requests that can fail. Use streams if possible.
- Make it clear to the clients whether they should reach out thr rpc guide or give up and file a bug.
- Allow clients to set deadlines.
- Rate limit using taphandler
- "With no limits, comes no memory"
- Limit max payload size (req/resp)

---

Also See:

- https://grpc.io/
- https://github.com/grpc-ecosystem/awesome-grpc
- https://github.com/hyperium/tonic

[^1]: https://graphql.org/
