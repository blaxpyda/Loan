### Advance Salary & Loan Calculator
This project implements a two-tier salary advance and loan calculator using FastAPI (backend) and Streamlit (frontend). It allows users to input their name, position, requested advance amount, and loan terms to generate an amortization schedule.

## Features
 - Position-based advance: Different advance approval factors per
    position (Junior, Mid, Senior, Lead).
 - Loan amortization: Calculates monthly payment, principal vs.     interest breakdown, and remaining balance.
 - Containerized: Backend and frontend run in separate Docker containers, orchestrated via Docker Compose.


## Prerequsites
 - Docker
 - Docker compose
 - Git

 ## Directory structure
 - ![Directory Structure](/assets/dir_structure.png)

 ## Setup and usage
 - Clone repo: `git clone https://github.com/blaxpyda/Loan.git`
 - cd <your repo>
 - Build and run with docker compose `docker compose up --build`
 - Acces the application at your local host

 - Conversely, you can access our depployed solution at `http://thugtheory.tech:8505/`
