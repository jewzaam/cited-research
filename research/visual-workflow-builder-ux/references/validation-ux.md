# Validation UX

Covers Dimension 5: inline canvas errors, pre-execution validation, connection type checking, runtime vs design-time error visualization.

See [citations.md](../citations.md) for full source details.

## Validation Approaches by Platform

| Tool | Design-Time Validation | Runtime Error Display | Error Handler Pattern |
|------|----------------------|----------------------|----------------------|
| Power Automate | Flow Checker — always active, red dot indicator [37] | Red highlights on erroneous actions [34] | Run-after settings for error paths [34] |
| n8n | Visual validation prevents invalid connections [13] | Execution log with status/timing [36] | Error workflows for automated failure response [36] |
| Zapier | Pre-publish checks | Run status in Zap history [38] | Custom error handler paths via three-dot menu [46] |
| Retool | Green highlighting during testing [7] | Block-level feedback | Branch blocks for conditional handling [7] |
| Microsoft Agent Framework | Type compatibility checks between executors [49] | Graph connectivity verification [49] | Edge validation for duplicates/invalids [49] |

## Power Automate Flow Checker

The most documented design-time validation system. Key behaviors [37]:

- **Always active**: Appears in command bar in the designer
- **Visual indicator**: Shows "a red dot when it finds one or more errors, potential errors, or warnings"
- **Auto-opens on save**: Activates automatically when saving with errors
- **Dual-location guidance**: "Red text from the checker" appears in both the Flow Checker panel and on the flow card
- **Fix workflow**: Select error → opens correction window

This represents the most thorough pre-execution validation among the tools studied.

## n8n Validation and Error Display

n8n uses multiple validation layers [13][36]:

- **Visual validation**: Prevents invalid node connections at design time [13]
- **Execution log**: Shows "latest execution time, status, mode, and running time" [36]
- **Error workflows**: Automated failure response — users configure how n8n responds to execution failures [36]

Known limitation: Activation validation errors display as "super vague" messages like "Validation Failed" with "zero context" — multiple GitHub issues track requests for better error messages (Agent C discovery, from search snippets).

## Zapier Error Handling

Zapier provides layered error management [38][46]:

- **Run status tracking**: All Zap runs receive status visible in history and editor [38]
- **AI-powered troubleshooting**: "Explains the issue and provides step-by-step instructions to resolve it" [38]
- **Autoreplay**: Automatically retries failed tasks from temporary issues [38]
- **Custom error handlers**: Three-dot menu → "Add error handler" → alternate Zap path [46]
- **Auto-disable**: "If a Zap errors repeatedly, it will automatically turn off" [38]

## Inline Validation UX Principles

General inline validation best practices applicable to workflow builders [44][45]:

- **Visual cues**: Color + icons indicate validation status — green checkmarks for valid, red exclamation for errors [44]
- **Timing challenge**: "We can't really validate just-in-time when errors occur because we can't really know for sure when the user has actually finished their input" [44]
- **Disruption risk**: "Constant feedback as users complete a form can be distracting, requiring users to repeatedly switch between form-filling and error-correcting mental modes" [44]
- **Error messages**: Should "clearly state what went wrong and possibly why, along with the next step" [45]

## Connection Type Checking

The Microsoft Agent Framework performs comprehensive validation [49]:
- Type compatibility checks ensuring message types are compatible between connected executors
- Graph connectivity verification
- Executor binding confirmation
- Edge validation for duplicate edges and invalid connections

This is the most sophisticated type-checking system found. Most workflow builders (n8n, Zapier) rely on runtime validation rather than design-time type checking between connections.

## Gaps and Limitations

- No standardized approach to connection type checking exists across workflow builders.
- Schema validation between workflow steps is poorly documented in public sources.
- Runtime vs design-time error visualization trade-offs have not been studied empirically.
- Agent C (primary researcher) was rate-limited; validation UX findings supplemented from search snippets and Power Automate/Zapier docs.
