from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Literal

app = FastAPI()

# Request and response models
class LoanRequest(BaseModel):
    name: str
    position: Literal["Junior", "Mid", "Senior", "Lead"]
    requested_amount: float
    annual_rate: float
    period_months: int

class AmorizationEntry(BaseModel):
    payment_number: int
    payment_amount: float
    principal_payment: float
    interest_payment: float
    remaining_balance: float

class LoanResponse(BaseModel):
    name: str
    position: str
    advance_amount: float
    schedule: List[AmorizationEntry]

# Approval factors
ADVANCE_FACTOR = {
    "Junior": 0.5,
    "Mid": 0.75,
    "Senior": 1.0,
    "Lead": 1.25
}

def compute_schedule(principal, annual_rate, n_months):
    r = annual_rate/100/12
    n = n_months
    if r == 0:
        payment = principal / n
    else:
        payment = principal * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
    balance = principal
    schedule = []
    for i in range(1, n+1):
        interest = balance * r
        principal_paid = payment - interest
        balance -= principal_paid
        schedule.append({
            "payment_number": i,
            "payment_amount": round(payment, 2),
            "principal_payment": round(principal_paid, 2),
            "interest_payment": round(interest, 2),
            "remaining_balance": round(max(balance, 0), 2)
        })
    return schedule

# Endpoint to handle loan requests
@app.post("/loan", response_model=LoanResponse)
def calculate_loan(req: LoanRequest):
    factor = ADVANCE_FACTOR.get(req.position)
    advance = req.requested_amount * factor
    if advance <= 0:
        raise HTTPException(status_code=400, detail="Invalid loan amount requested.")
    schedule = compute_schedule(advance, req.annual_rate, req.period_months)
    return LoanResponse(
        name=req.name,
        position=req.position,
        advance_amount=round(advance, 2),
        schedule=schedule
    )
