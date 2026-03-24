from algopy import ARC4Contract, String, UInt64
from algopy.arc4 import abimethod


class AlgosphereCore(ARC4Contract):

    @abimethod()
    def log_alert(self, risk_level: String, risk_score: UInt64, reason: String) -> String:
        return String("Alert logged: ") + risk_level

    @abimethod()
    def hello(self, name: String) -> String:
        return String("Hello from AlgoSphere, ") + name
