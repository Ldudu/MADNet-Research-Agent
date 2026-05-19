# Sample Request

## Input question

What are the main open issues in remote sensing VSR, and which of them are caused by unrealistic degradation assumptions?

## Expected workflow behavior

1. `Planner` decomposes the question into open problems, degradation realism, evaluation assumptions, and evidence gaps.
2. `Retriever` recalls papers that mention degradation, real-world mismatch, evaluation, and benchmark design.
3. `Analyst` extracts recurring problem patterns and comparable dimensions.
4. `Critic` checks whether the evidence is broad enough to support the conclusion.
5. `Writer` produces a report, trace, and summary.

## Expected reviewer value

- The result is not just an answer.
- The reasoning path is explicit.
- The evidence basis can be reviewed independently.
