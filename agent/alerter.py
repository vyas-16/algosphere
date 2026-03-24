import sys
sys.path.append("/Users/pallavi/AlgoSphere/agent")
from agent import analyze_risk

def run_agent():
    print("AlgoSphere DeFi Guardian started...")
    print("Analyzing live market data...")
    result = analyze_risk()
    print("Risk Level: " + result["risk_level"])
    print("Risk Score: " + str(result["risk_score"]) + "/10")
    print("Reason: " + result["reason"])
    print("Recommendation: " + result["recommendation"])
    print("Alert logged on Algorand blockchain!")

if __name__ == "__main__":
    run_agent()