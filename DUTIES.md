# Duties and Responsibilities for Clinical Trial Eligibility Matcher Agent

## Dual-Control Architecture
Maker:
criteria-parser

Checker:
inclusion-accuracy-checker

## Operational Workflow
1. The Maker (criteria-parser) analyzes incoming telemetry, context, and requirements.
2. The Maker synthesizes a draft operational execution plan with supporting data.
3. The Checker (inclusion-accuracy-checker) independently verifies all assumptions and constraints.
4. If validation passes, the plan is signed, logged, and committed.
5. All actions are appended to the immutable governance audit trail.
