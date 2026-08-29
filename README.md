# Python Coursework Exercises

Small standalone exercises from my Foundation Year Computer Science
coursework (De Montfort University Kazakhstan, Computing Pathway).

These are short, individually simple scripts practicing one concept each,
plus three slightly larger exercises split across multiple linked modules
— not standalone projects. Included here to show ongoing, hands-on
practice with core Python fundamentals alongside the larger
[Auth Log Analyzer](https://github.com/AndreyDya/Auth-log-analyzer) project.

## Single-file exercises

| File | Concept practiced |
|---|---|
| `oop_dog.py` | Classes, `__init__`, methods |
| `shopping_cart.py` | Lists of tuples, loops, running totals |
| `volume_calc.py` | Functions with multiple parameters |
| `math_helpers_module.py` | Writing a reusable module of functions |
| `import_and_use_module.py` | Importing and using functions from a module you wrote yourself |
| `calc_compound_interest.py` | Basic arithmetic / formulas in code |
| `password_validator_tests.py` | Writing test cases before/alongside a function |
| `contestant_intro_cards.py` | Loops, lists of dictionaries, formatted string output |
| `speeding_ticket_calc.py` | Unit conversion, if/elif tiers, input validation loop |
| `sports_hall_cost_calc.py` | Nested loops, tiered pricing logic, confirm/retry input flow |
| `olympic_rings.py` | Circle geometry (`turtle`), trigonometry for arc placement, layered drawing |

## Multi-module exercises

**`parcel-sorter/`** — reads a list of parcel weights, sorts them with a
hand-written quicksort implementation, and reports the lightest.
Split across `main.py`, `input_handling.py`, `sorting.py`, `display.py`,
and `config.py` to practice separating input, logic, and output.

**`word-reversal/`** — validates and reformats a sentence (reverses word
order). Split across `P6.py`, `P6_user_input.py`,
`P6_input_validation.py`, `P6_format_sentence.py`, and `P6_config.py`
for the same reason.

**`tkinter-registration-form/`** — three incremental steps building up a
basic Tkinter GUI form: an empty window, then labeled input fields laid
out with `.grid()`, then a submit button with basic email validation.
Kept as separate numbered files to show the progression rather than
just the final result.
