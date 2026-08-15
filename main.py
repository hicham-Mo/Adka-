from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os, sys, json, requests
from noor_core.experts_data import get_advanced_experts
from core.experts_logic import get_expert_response
from core.wisdom_engine import wisdom_engine

app = FastAPI(title="NOOR OMNI v172 - Sovereign Intelligence", version="172.2")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

def get_market():
    try:
        r = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=mad", timeout=2).json()
        price = r['ethereum']['mad']
        return {"total": f"{172.77 * price:,.2f}", "status": "LIVE ✅"}
    except:
        return {"total": "4,600,000.00", "status": "OFFLINE ⚠️"}

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    financial_data = wisdom_engine.analyze_financial_sovereignty()
    return templates.TemplateResponse(
        request=request, 
        name="dashboard.html", 
        context={
            "market": get_market(), 
            "experts": get_advanced_experts(), 
            "financial": financial_data,
            "version": "172.2"
        }
    )

@app.post("/", response_class=HTMLResponse)
async def handle(request: Request, expert_name: str = Form(None), user_query: str = Form(None)):
    res = ""
    if expert_name and user_query:
        res = get_expert_response(expert_name, user_query)
    elif user_query and not expert_name:
        res = get_expert_response("المراقب السيادي", user_query)

    financial_data = wisdom_engine.analyze_financial_sovereignty()
    return templates.TemplateResponse(
        request=request, 
        name="dashboard.html", 
        context={
            "market": get_market(), 
            "experts": get_advanced_experts(), 
            "expert_res": res, 
            "selected_expert": expert_name, 
            "financial": financial_data,
            "version": "172.2"
        }
    )

@app.get("/api/v1/sovereignty/health")
def health_check():
    return {
        "status": "HEALTHY",
        "protocol": 1372,
        "financial_sovereignty": wisdom_engine.analyze_financial_sovereignty(),
        "legal_status": wisdom_engine.Legal_compliance_check()
    }

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
